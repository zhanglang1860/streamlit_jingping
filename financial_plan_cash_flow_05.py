#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Zhangyicheng
@file:financial_plan_cash_flow_05.py
@time:2020/11/17
"""

from loan_interest_04 import *


class FinancialPlanCashFlow(LoanInterest):
    def default(self):
        FinancialPlanCashFlow.__init__(self)

    def __init__(self, df_01, df_02, df_03, df_04, **kargs):
        LoanInterest.__init__(self, df_01, df_02, df_03, run_time=1, capacity_mw=kargs['capacity_mw'],
                             eleprice=kargs['eleprice'], investment=kargs['investment'],
                             annual_effective_hours=kargs['annual_effective_hours'])

        self.df_04_f = df_04
        self.df_04_f['合计'] = 0



        self.营业收入 = self.df_03_f.loc[pd.IndexSlice['1', '营业收入']]
        self.营业税金附加 = self.df_03_f.loc[pd.IndexSlice['2', '营业税金附加']]
        self.所得税 = self.df_03_f.loc[pd.IndexSlice['8', '所得税']]

        # self.经营成本 = [0.00, 0.00, 617.90, 617.90, 617.90, 775.40, 775.40, 775.40, 775.40, 775.40, 932.90, 932.90, 932.90,
        #              932.90, 932.90, 932.90, 932.90, 1090.40, 1090.40, 1090.40, 1090.40, 1090.40]
        self.经营成本 = self.df_02_f.loc[pd.IndexSlice['12', '经营成本']]

        # self.建设投资 = [0.00, 35000.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
        #              0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
        self.建设投资 = self.df_01_f.loc[pd.IndexSlice['1.1', '建设投资']]

        # self.流动资金 = [0.00, 0.00, 150.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
        #              0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
        self.流动资金 = self.df_01_f.loc[pd.IndexSlice['1.3', '流动资金']]

        # self.项目资本金投入 = [0, 7164.23, 45.00, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.项目资本金投入 = self.df_01_f.loc[pd.IndexSlice['2.1', '资本金（资金筹措）']]

        # self.建设投资借款 = [0, 27835.77, 0.00, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.建设投资借款 = self.df_01_f.loc[pd.IndexSlice['2.2.1.1', '长期借款本金']]

        # self.流动资金借款 = [0, 0.00, 105.00, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.流动资金借款 = self.df_01_f.loc[pd.IndexSlice['2.2.2', '流动资金借款']]

        # self.短期借款 = [0, 0.00, 174.05, 238.85, 188.22, 182.05, 56.43, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
        #              0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
        self.短期借款 = self.df_04_f.loc[pd.IndexSlice['3', '短期借款']]

        # self.各种利息支出 = [0.00, 0.00, 1705.69, 1596.44, 1481.01, 1367.96, 1248.53, 1132.79, 1020.07, 907.36, 794.64,
        #                681.92, 569.20, 456.49, 343.77, 231.05, 118.33, 5.62, 5.62, 5.62, 5.62, 5.62]
        self.各种利息支出 = self.df_04_f.loc[pd.IndexSlice['3.5', '利息支出']]

        # self.本年还本 = [0.00, 0.00, 1910.46, 1910.46, 1910.46, 1910.46, 1910.46, 1910.46, 1910.46, 1910.46, 1910.46,
        #              1910.46, 1910.46, 1910.46, 1910.46, 1910.46, 1910.46, 0.00, 0.00, 0.00, 0.00, 0.00]
        self.本年还本 = self.df_04_f.loc[pd.IndexSlice['1.2.1', '本年还本']]

        # self.偿还流动资金借款本金 = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
        #                    0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 105.00]
        self.偿还流动资金借款本金 = self.df_04_f.loc[pd.IndexSlice['2.3', '偿还流动资金借款本金']]

        # self.偿还短期借款本金 = [0.00, 0.00, 0.00, 174.05, 238.85, 188.22, 182.05, 56.43, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
        #                  0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
        self.偿还短期借款本金 = self.df_04_f.loc[pd.IndexSlice['3.1', '偿还短期借款本金']]

        # self.应付利润 = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 59.82, 559.93,
        #              576.74, 576.74, 576.74, 576.74, 576.74, 576.74]
        self.应付利润 = self.df_03_f.loc[pd.IndexSlice['16', '应付利润']]

        self.columns_name_05 = ['第0年','第1年', '第2年', '第3年', '第4年', '第5年', '第6年', '第7年', '第8年', '第9年', '第10年', '第11年',
                                '第12年', '第13年', '第14年', '第15年', '第16年', '第17年', '第18年', '第19年', '第20年', '第21年']

        # columns_name=[i for i in range(1,22)]
        self.index_name0_05 = ['1', '1.1', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.2', '1.2.1', '1.2.2', '1.2.3',
                               '1.2.4', '1.2.5', '1.2.6', '2', '2.1', '2.2', '2.2.1', '2.2.2', '2.2.3', '3', '3.1',
                               '3.1.1', '3.1.2', '3.1.3', '3.1.4', '3.1.5', '3.1.6', '3.2', '3.2.1', '3.2.2', '3.2.3',
                               '3.2.4', '4', '5']
        self.index_name1_05 = ['经营活动净现金流量', '现金流入01', '营业收入', '增值税销项税额', '补贴收入(不含增值税优惠)', '其他流入01',
                               '现金流出01', '经营成本', '增值税进项税额', '营业税金附加', '增值税', '所得税', '其他流出01',
                               '投资活动净现金流量', '现金流入02', '现金流出02', '建设投资', '流动资金', '其他流出02',
                               '筹资活动净现金流量', '现金流入03', '项目资本金投入', '建设投资借款', '流动资金借款', '债券', '短期借款', '其他流入03',
                               '现金流出03', '各种利息支出', '偿还债务本金', '应付利润（股利分配）', '其他流出03', '净现金流量', '累计盈余资金', ]

        self.df_05 = pd.DataFrame(
            np.zeros(len(self.index_name1_05) * len(self.columns_name_05)).reshape(
                (len(self.index_name1_05), len(self.columns_name_05))))
        self.df_05 = self.df_05.T
        self.df_05.columns = self.index_name1_05
    def cal_df_05(self):
        self.df_05['营业收入'] = self.营业收入
        self.df_05['增值税销项税额'] = self.增值税
        self.df_05['补贴收入(不含增值税优惠)'] = 0
        self.df_05['其他流入01'] = 0
        self.df_05['现金流入01'] = self.df_05['营业收入'] + self.df_05['增值税销项税额'] + self.df_05['补贴收入(不含增值税优惠)'] + self.df_05[
            '其他流入01']

        self.df_05['经营成本'] = self.经营成本
        self.df_05['增值税进项税额'] = 0
        self.df_05['营业税金附加'] = self.营业税金附加

        for ind, row in self.df_05.iterrows():
            row['增值税销项税额加总'] = self.df_05.loc[self.df_05.index <= ind, '增值税销项税额'].sum()
            if row['增值税销项税额加总'] <= self.tax_deduction:
                self.df_05.loc[ind, '增值税'] = 0
            else:
                self.df_05.loc[ind, '增值税'] = (row['增值税销项税额加总'] - self.tax_deduction) / 2 \
                                             - self.df_05.loc[self.df_05.index < ind, '增值税'].sum()
        self.df_05['所得税'] = self.所得税
        self.df_05['其他流出01'] = 0
        self.df_05['现金流出01'] = self.df_05['经营成本'] + self.df_05['增值税进项税额'] + self.df_05['营业税金附加'] + self.df_05['增值税'] + \
                               self.df_05['所得税'] + self.df_05['其他流出01']
        self.df_05['经营活动净现金流量'] = self.df_05['现金流入01'] - self.df_05['现金流出01']

        # '投资活动净现金流量'
        self.df_05['现金流入02'] = 0
        self.df_05['建设投资'] = self.建设投资
        self.df_05['流动资金'] = self.流动资金
        self.df_05['其他流出02'] = 0
        self.df_05['现金流出02'] = self.df_05['建设投资'] + self.df_05['流动资金'] + self.df_05['其他流出02']
        self.df_05['投资活动净现金流量'] = self.df_05['现金流入02'] - self.df_05['现金流出02']

        # 筹资活动净现金流量

        self.df_05['项目资本金投入'] = self.项目资本金投入
        self.df_05['建设投资借款'] = self.建设投资借款
        self.df_05['流动资金借款'] = self.流动资金借款
        self.df_05['债券'] = 0
        self.df_05['短期借款'] = self.短期借款
        self.df_05['其他流入03'] = 0

        self.df_05['各种利息支出'] = self.各种利息支出

        self.df_05['本年还本'] = self.本年还本
        self.df_05['偿还流动资金借款本金'] = self.偿还流动资金借款本金
        self.df_05['偿还短期借款本金'] = self.偿还短期借款本金

        self.df_05['偿还债务本金'] = self.df_05['本年还本'] + self.df_05['偿还流动资金借款本金'] + self.df_05['偿还短期借款本金']
        self.df_05['应付利润（股利分配）'] = self.应付利润
        self.df_05['其他流出03'] = 0

        self.df_05['现金流入03'] = self.df_05['项目资本金投入'] + self.df_05['建设投资借款'] + self.df_05['流动资金借款'] + self.df_05['债券'] + \
                               self.df_05[
                                   '短期借款'] + self.df_05['其他流入03']
        self.df_05['现金流出03'] = self.df_05['各种利息支出'] + self.df_05['偿还债务本金'] + self.df_05['应付利润（股利分配）'] + self.df_05[
            '其他流出03']
        self.df_05['筹资活动净现金流量'] = self.df_05['现金流入03'] - self.df_05['现金流出03']

        self.df_05['净现金流量'] = self.df_05['经营活动净现金流量'] + self.df_05['投资活动净现金流量'] + self.df_05['筹资活动净现金流量']

        for ind, row in self.df_05.iterrows():
            self.df_05.loc[ind, '累计盈余资金'] = self.df_05.loc[self.df_05.index <= ind, '净现金流量'].sum()

        self.df_05 = self.df_05[self.index_name1_05]
        self.df_05 = self.df_05.T
        self.df_05.columns = self.columns_name_05

        self.df_05['项目'] = self.df_05.index
        self.df_05['序号'] = self.index_name0_05
        self.df_05.set_index(['序号', '项目'], inplace=True)
        self.df_05=self.df_05.fillna(0)
        self.df_05.insert(0, '合计', self.df_05.sum(axis=1))
        self.df_05=self.df_05.drop(columns=self.df_05.columns[1])
        return self.df_05


if __name__ == '__main__':
    # pd.set_option('display.unicode.ambiguous_as_wide', True)
    # pd.set_option('display.unicode.east_asian_width', True)
    # a = FinancialPlanCashFlow()
    # a.cal_profit()
    # df_05 = a.cal_cash_flow()
    # writer = pd.ExcelWriter('FinancialPlanCashFlow.xlsx')
    # df_05.to_excel(writer, float_format='%.5f')
    # writer.save()

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

    print(result_05.iloc[:, :4])
