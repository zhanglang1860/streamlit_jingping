#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Zhangyicheng
@file:balance_sheet_09.py
@time:2020/11/20
"""
from funds_statement_08 import *


class BalanceSheet(FundsStatement):
    def default(self):
        BalanceSheet.__init__(self)

    def __init__(self, df_01, df_02, df_03, df_04, df_05, df_06, df_07, df_08, **kargs):
        FundsStatement.__init__(self, df_01, df_02, df_03, df_04, df_05, df_06, df_07, run_time=1,
                                capacity_mw=kargs['capacity_mw'], eleprice=kargs['eleprice'],
                                investment=kargs['investment'], annual_effective_hours=kargs['annual_effective_hours'])
        self.df_08_f = df_08
        self.df_08_f['合计'] = 0
        self.累计盈余资金_资金来源与运用表 = self.df_08_f.loc[pd.IndexSlice['4', '累计盈余资金']]
        self.本年短期借款 = self.短期借款

        self.年初借款余额 = self.df_04_f.loc[pd.IndexSlice['1.1', '年初借款余额']]
        self.流动资金借款累计_借款还本付息计划表 = self.df_04_f.loc[pd.IndexSlice['2.1', '流动资金借款累计']]
        self.提取法定盈余公积金 = self.df_03_f.loc[pd.IndexSlice['13', '提取法定盈余公积金']]
        self.未分配利润 = self.df_03_f.loc[pd.IndexSlice['17', '未分配利润（14-15-16）']]

        self.columns_name_09 = ['第0年', '第1年', '第2年', '第3年', '第4年', '第5年', '第6年', '第7年', '第8年', '第9年', '第10年', '第11年',
                                '第12年', '第13年', '第14年', '第15年', '第16年', '第17年', '第18年', '第19年', '第20年', '第21年']

        self.index_name0_09 = ['1', '1.1', '1.1.1', '1.1.2', '1.2', '1.3', '1.4', '1.5', '2', '2.1', '2.1.1', '2.1.2',
                               '2.2', '2.3', '2.4', '2.5', '2.5.1', '2.5.2', '2.5.3', '2.5.4', '2.5.5','3']
        self.index_name1_09 = ['资产', '流动资产总额', '累计盈余资金', '流动资产',
                               '在建工程', '固定资产净值', '无形及其他资产净值', '可抵扣增值税形成资产',
                               '负债及所有者权益（2.4+2.5）', '流动负债总额', '本年短期借款',
                               '其他', '建设投资借款', '流动资金借款', '负债小计（2.1+2.2+2.3）',
                               '所有者权益', '资本金', '资本公积', '累计盈余公积金', '累计未分配利润', '资产负债平衡','资产负债率'
                               ]

        self.df_09 = pd.DataFrame(
            np.zeros(len(self.index_name1_09) * len(self.columns_name_09)).reshape(
                (len(self.index_name1_09), len(self.columns_name_09))))

        self.df_09 = self.df_09.T
        self.df_09.columns = self.index_name1_09

    def cal_balance_sheet(self):

        self.df_09['回收流动资金'] = self.回收流动资金
        self.df_09['累计盈余资金_资金来源与运用表'] = self.累计盈余资金_资金来源与运用表
        self.df_09['累计盈余资金_资产负债表'] = self.df_09['累计盈余资金_资金来源与运用表'] - self.df_09['回收流动资金']
        self.df_09['累计盈余资金'] = self.df_09['累计盈余资金_资产负债表']
        self.df_09['流动资产'] = self.流动资金.loc[2]
        self.df_09.loc[0:1, '流动资产'] = 0
        self.df_09['流动资产总额'] = self.df_09['累计盈余资金'] + self.df_09['流动资产']

        self.df_09['建设投资'] = self.建设投资
        self.df_09['建设期利息'] = self.建设期利息
        self.df_09['在建工程'] = self.df_09['建设投资'] + self.df_09['建设期利息']

        self.df_09['折旧费'] = self.折旧费
        for ind, row in self.df_09.iterrows():
            if ind == 1:
                self.df_09.loc[ind, '固定资产净值'] = 0
            else:
                self.df_09.loc[ind, '固定资产净值'] = self.df_09['折旧费'].sum() - self.df_09.loc[
                    self.df_09.index <= ind, '折旧费'].sum()
        self.df_09['无形及其他资产净值'] = 0

        self.df_09['增值税_利润和利润分配表'] = self.增值税
        for ind, row in self.df_09.iterrows():
            if ind == 1:
                self.df_09.loc[ind, '可抵扣增值税形成资产'] = 0
            elif self.tax_deduction >= self.df_09.loc[self.df_09.index <= ind, '增值税_利润和利润分配表'].sum():
                self.df_09.loc[ind, '可抵扣增值税形成资产'] = self.tax_deduction - self.df_09.loc[
                    self.df_09.index <= ind, '增值税_利润和利润分配表'].sum()
            else:
                self.df_09.loc[ind, '可抵扣增值税形成资产'] = 0

        self.df_09['资产'] = self.df_09['流动资产总额'] + self.df_09['在建工程'] + self.df_09['固定资产净值'] \
                           + self.df_09['无形及其他资产净值'] + self.df_09['可抵扣增值税形成资产']

        self.df_09['本年短期借款'] = self.本年短期借款
        self.df_09['其他'] = 0
        self.df_09['流动负债总额'] = self.df_09['本年短期借款'] + self.df_09['其他']
        self.df_09['流动资金借款累计'] = self.流动资金借款累计_借款还本付息计划表
        self.df_09['偿还流动资金借款本金'] = self.偿还流动资金借款本金
        self.df_09['流动资金借款'] = self.df_09['流动资金借款累计'] - self.df_09['偿还流动资金借款本金']

        self.df_09['资本金_投资计划与资金筹措表'] = self.资本金_投资计划与资金筹措表
        self.df_09['提取法定盈余公积金'] = self.提取法定盈余公积金

        for ind, row in self.df_09.iterrows():
            if ind < self.df_09.shape[0]-1 and ind != 0:
                self.df_09.loc[ind, '建设投资借款'] = self.年初借款余额.iloc[ind + 1]
            else:
                self.df_09.loc[ind, '建设投资借款'] = 0
            self.df_09.loc[ind, '资本金'] = self.df_09.loc[self.df_09.index <= ind, '资本金_投资计划与资金筹措表'].sum()
            self.df_09.loc[ind, '累计盈余公积金'] = self.df_09.loc[self.df_09.index <= ind, '提取法定盈余公积金'].sum()
        self.df_09['资本公积'] = 0


        self.df_09['累计未分配利润'] = self.未分配利润

        self.df_09['所有者权益'] = self.df_09['资本金'] + self.df_09['资本公积'] + self.df_09['累计盈余公积金'] + self.df_09['累计未分配利润']
        self.df_09['负债小计（2.1+2.2+2.3）'] = self.df_09['流动负债总额'] + self.df_09['建设投资借款'] + self.df_09['流动资金借款']
        self.df_09['负债及所有者权益（2.4+2.5）'] = self.df_09['负债小计（2.1+2.2+2.3）'] + self.df_09['所有者权益']

        self.df_09['资产负债平衡'] = self.df_09['资产'] - self.df_09['负债及所有者权益（2.4+2.5）']
        self.df_09['资产负债率'] = self.df_09['负债小计（2.1+2.2+2.3）'] / self.df_09['资产' \
                                                                           '']


        self.df_09 = self.df_09[self.index_name1_09]
        self.df_09 = self.df_09.T
        self.df_09.columns = self.columns_name_09
        self.df_09['项目'] = self.df_09.index
        self.df_09['序号'] = self.index_name0_09
        self.df_09.set_index(['序号', '项目'], inplace=True)
        self.df_09 = self.df_09.iloc[:, 1:]
        self.df_09.insert(0, '合计', self.df_09.sum(axis=1))
        return self.df_09

    def cal_df_09(self):

        self.df_09 = self.cal_balance_sheet()

        return self.df_09


if __name__ == '__main__':
    # pd.set_option('display.unicode.ambiguous_as_wide', True)
    # pd.set_option('display.unicode.east_asian_width', True)
    # a = BalanceSheet()
    # a.cal_profit()
    # df_09 = a.cal_balance_sheet()
    # writer = pd.ExcelWriter('BalanceSheet.xlsx')
    # df_09.to_excel(writer, float_format='%.5f')
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
    # print(result_09.iloc[:, 1:2])
