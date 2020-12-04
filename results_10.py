#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ZhangYicheng
@file:results_10.py
@time:2020/11/24
"""
from balance_sheet_09 import *


class Results(BalanceSheet):
    def default(self):
        Results.__init__(self)

    def __init__(self, df_01, df_02, df_03, df_04, df_05, df_06, df_07, df_08, df_09, **kargs):
        BalanceSheet.__init__(self, df_01, df_02, df_03, df_04, df_05, df_06, df_07, df_08, run_time=1,
                              capacity_mw=kargs['capacity_mw'], eleprice=kargs['eleprice'],
                              investment=kargs['investment'], annual_effective_hours=kargs['annual_effective_hours'])
        self.df_09_f = df_09
        self.df_09_f['合计'] = 0

        self.columns_name = ['数值']

        self.index_name0 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                            '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', ]

        self.index_name1 = ['装机容量', '年上网电量', '总投资', '建设期利息', '流动资金', '销售收入总额(不含增值税)',
                            '总成本费用', '营业税金附加总额', '发电利润总额', '经营期平均电价（不含增值税）',
                            '经营期平均电价（含增值税）', '项目投资回收期（所得税前）', '项目投资回收期（所得税后）', '项目投资财务内部收益率（所得税前）',
                            '项目投资财务内部收益率（所得税后）', '项目投资财务净现值（所得税前）', '项目投资财务净现值（所得税后）',
                            '资本金财务内部收益率', '资本金财务净现值', '总投资收益率（ROI）', '投资利税率', '项目资本金净利润率（ROE）',
                            '资产负债率（最大值）',
                            '盈亏平衡点（生产能力利用率）', '盈亏平衡点（年产量）', ]

        self.df = pd.DataFrame(
            np.zeros(len(self.index_name1) * len(self.columns_name)).reshape(
                (len(self.index_name1), len(self.columns_name))))
        self.df = self.df.T
        self.df.columns = self.index_name1

    def cal_df_10(self):
        self.df['装机容量'] = self.capacity_mw
        self.df['年上网电量'] = self.df_03_f.loc[pd.IndexSlice['0', '上网电量（MWh）']].sum() / (self.cal_y - self.building_y)
        self.df['总投资'] = self.df_01_f.loc[pd.IndexSlice['1', '总投资']].sum()
        self.df['建设期利息'] = sum(self.建设期利息)
        self.df['流动资金'] = self.流动资金.sum()
        self.df['销售收入总额(不含增值税)'] = self.df_03_f.loc[pd.IndexSlice['1', '营业收入']].sum()
        self.df['总成本费用'] = self.df_02_f.loc[pd.IndexSlice['11', '总成本费用']].sum()
        self.df['营业税金附加总额'] = self.df_03_f.loc[pd.IndexSlice['2', '营业税金附加']].sum()
        self.df['发电利润总额'] = self.df_03_f.loc[pd.IndexSlice['5', '利润总额（1-2-3+4）']].sum()
        self.df['经营期平均电价（不含增值税）'] = self.df_03_f.loc[pd.IndexSlice['0.1', '电价（不含增值税）（元/kWh）'], 1]

        self.df['经营期平均电价（含增值税）'] = self.df_03_f.loc[pd.IndexSlice['0.2', '电价（含增值税）（元/kWh）'], 1]
        self.df['项目投资回收期（所得税前）'] = self.df_06_f.loc[pd.IndexSlice['10', '项目投资回收期（所得税前）'], 1]
        self.df['项目投资回收期（所得税后）'] = self.df_06_f.loc[pd.IndexSlice['11', '项目投资回收期（所得税后）'], 1]
        self.df['项目投资财务内部收益率（所得税前）'] = self.df_06_f.loc[pd.IndexSlice['12', '项目投资财务内部收益率（所得税前）'], 1] * 100
        self.df['项目投资财务内部收益率（所得税后）'] = self.df_06_f.loc[pd.IndexSlice['13', '项目投资财务内部收益率（所得税后）'], 1] * 100
        self.df['项目投资财务净现值（所得税前）'] = self.df_06_f.loc[pd.IndexSlice['8', '项目投资财务净现值（所得税前）'], 1]
        self.df['项目投资财务净现值（所得税后）'] = self.df_06_f.loc[pd.IndexSlice['9', '项目投资财务净现值（所得税后）'], 1]
        self.df['资本金财务内部收益率'] = self.df_07_f.loc[pd.IndexSlice['7', '资本金财务内部收益率'], 1] * 100
        self.df['资本金财务净现值'] = self.df_07_f.loc[pd.IndexSlice['9', '资本金财务净现值'], 1]
        self.df['总投资收益率（ROI）'] = self.df_03_f.loc[pd.IndexSlice['18', '息税前利润（利润总额+利息支出）']].sum() / (
                self.cal_y - self.building_y) / self.df['总投资'] * 100

        self.df['投资利税率'] = (self.df['营业税金附加总额'] + self.df['发电利润总额']) / (self.cal_y - self.building_y) / self.df[
            '总投资'] * 100

        self.df['项目资本金净利润率（ROE）'] = self.df_03_f.loc[pd.IndexSlice['10', '净利润（5-8+9）']].sum() / (
                self.cal_y - self.building_y) / self.df_01_f.loc[pd.IndexSlice['2.1', '资本金（资金筹措）']].sum() * 100

        self.df['资产负债率（最大值）'] = self.df_09_f.loc[pd.IndexSlice['3', '资产负债率']].max() * 100
        self.df['盈亏平衡点（生产能力利用率）'] = self.df_02_f.loc[pd.IndexSlice['9', '固定成本']].sum() / (
                self.df['销售收入总额(不含增值税)'] - self.df['营业税金附加总额'] - self.df_02_f.loc[
            pd.IndexSlice['10', '可变成本']].sum()) * 100

        self.df['盈亏平衡点（年产量）'] = self.df['年上网电量'] * self.df['盈亏平衡点（生产能力利用率）'] / 100

        self.df_10 = self.df.T

        self.df_10.columns = self.columns_name
        self.df_10['项目'] = self.df_10.index
        self.df_10['序号'] = self.index_name0
        unit = ['MW', 'MW', '万元', '万元', '万元', '万元', '万元', '万元', '万元', '元/kWh', '元/kWh', '年',
                '年', '%', '%', '万元', '万元', '%', '万元', '%', '%', '%', '%', '%', 'MWh', ]

        self.df_10.set_index(['序号', '项目'], inplace=True)
        self.df_10.insert(0, '单位', unit)
        return self.df_10


if __name__ == '__main__':
    real_01 = InvestmentFinancing(run_time=1, capacity_mw=50, eleprice=0.29, investment=35000,
                                  annual_effective_hours=2800)
    result_01 = real_01.cal_df_01()

    real_02 = TotalCost(result_01, run_time=1, capacity_mw=50, eleprice=0.29, investment=35000,
                        annual_effective_hours=2800)
    result_02 = real_02.cal_df_02()

    real_03 = ProfitTable(result_01, result_02, run_time=1, capacity_mw=50, eleprice=0.29, investment=35000,
                          annual_effective_hours=2800)
    result_03 = real_03.cal_df_03()

    real_04 = LoanInterest(result_01, result_02, result_03, run_time=1, capacity_mw=50, eleprice=0.29, investment=35000,
                           annual_effective_hours=2800)
    result_04 = real_04.cal_df_04()

    real_05 = FinancialPlanCashFlow(result_01, result_02, result_03, result_04, run_time=1, capacity_mw=50,
                                    eleprice=0.29, investment=35000, annual_effective_hours=2800)
    result_05 = real_05.cal_df_05()

    real_06 = InvestmentCF(result_01, result_02, result_03, result_04, result_05, run_time=1, capacity_mw=50,
                           eleprice=0.29, investment=35000, annual_effective_hours=2800)
    result_06 = real_06.cal_df_06()

    real_07 = CapitalCF(result_01, result_02, result_03, result_04, result_05, result_06, run_time=1, capacity_mw=50,
                        eleprice=0.29, investment=35000, annual_effective_hours=2800)
    result_07 = real_07.cal_df_07()

    real_08 = FundsStatement(result_01, result_02, result_03, result_04, result_05, result_06, result_07, run_time=1,
                             capacity_mw=50,
                             eleprice=0.29, investment=35000, annual_effective_hours=2800)
    result_08 = real_08.cal_df_08()

    real_09 = BalanceSheet(result_01, result_02, result_03, result_04, result_05, result_06, result_07, result_08,
                           run_time=1, capacity_mw=50, eleprice=0.29, investment=35000, annual_effective_hours=2800)
    result_09 = real_09.cal_df_09()

    real_10 = Results(result_01, result_02, result_03, result_04, result_05, result_06, result_07, result_08, result_09,
                      run_time=1, capacity_mw=50, eleprice=0.29, investment=35000, annual_effective_hours=2800)
    result_10 = real_10.cal_df_10()

    print(result_10)
