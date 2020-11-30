#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ZhangYicheng
@file:funds_statement_08.py
@time:2020/11/23
"""

from capital_cf_07 import *


class FundsStatement(CapitalCF):
    def default(self):
        FundsStatement.__init__(self)

    def __init__(self, df_01, df_02, df_03, df_04, df_05, df_06,df_07, **kargs):
        CapitalCF.__init__(self, df_01, df_02, df_03, df_04, df_05,df_06, run_time=1, capacity_mw=kargs['capacity_mw'],
                              eleprice=kargs['eleprice'], investment=kargs['investment'],
                              annual_effective_hours=kargs['annual_effective_hours'])
        self.df_07_f = df_07
        self.df_07_f['合计'] = 0


        self.利润总额 = self.df_03_f.loc[pd.IndexSlice['5', '利润总额（1-2-3+4）']]
        self.折旧费 = self.df_02_f.loc[pd.IndexSlice['1', '折旧费']]
        self.摊销费 = self.df_02_f.loc[pd.IndexSlice['6', '摊销费']]
        self.长期借款 = self.df_04_f.loc[pd.IndexSlice['1', '长期借款']]
        self.流动资金借款_借款还本付息计划表 = self.df_04_f.loc[pd.IndexSlice['2', '流动资金借款']]
        self.回收固定资产余值 = self.df_06_f.loc[pd.IndexSlice['1.3', '回收固定资产余值']]
        self.回收流动资金 = self.df_06_f.loc[pd.IndexSlice['1.4', '回收流动资金']]
        self.建设投资 = self.df_01_f.loc[pd.IndexSlice['1.1', '建设投资']]

        # self.建设期利息 = [0.00, 821.16, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
        #               0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
        # self.建设期利息 = self.df_01_f.loc[pd.IndexSlice['1.2', '建设期利息']]


        self.columns_name_08 = ['第0年', '第1年', '第2年', '第3年', '第4年', '第5年', '第6年', '第7年', '第8年', '第9年', '第10年', '第11年',
                             '第12年', '第13年', '第14年', '第15年', '第16年', '第17年', '第18年', '第19年', '第20年', '第21年']

        self.index_name0_08 = ['1', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6',
                            '1.7', '1.8', '1.9', '1.10', '2', '2.1', '2.2', '2.3',
                            '2.4', '2.5', '2.6', '2.7', '3', '4', ]

        self.index_name1_08 = ['资金来源', '利润总额', '折旧费', '摊销费', '长期借款', '流动资金借款',
                            '其他短期借款', '资本金', '其他01', '回收固定资产余值', '回收流动资金',
                            '资金运用', '固定资产投资', '建设期利息', '流动资金', '所得税', '应付利润',
                            '借款本金偿还', '其他02', '盈余资金（1-2）', '累计盈余资金', ]

        self.df_08 = pd.DataFrame(
            np.zeros(len(self.index_name1_08) * len(self.columns_name_08)).reshape(
                (len(self.index_name1_08), len(self.columns_name_08))))
        self.df_08 = self.df_08.T
        self.df_08.columns = self.index_name1_08


    def cal_funds_statement(self):
        self.df_08['利润总额'] = self.利润总额
        self.df_08['折旧费'] = self.折旧费
        self.df_08['摊销费'] = self.摊销费
        self.df_08['长期借款'] = self.长期借款
        self.df_08['流动资金借款'] = self.流动资金借款_借款还本付息计划表
        self.df_08['其他短期借款'] = self.短期借款
        self.df_08['资本金'] = self.资本金_投资计划与资金筹措表

        self.df_08['其他01'] = 0

        self.df_08['增值税_利润和利润分配表'] = self.增值税
        for ind, row in self.df_08.iterrows():
            if self.df_08.loc[self.df_08.index <= ind, '增值税_利润和利润分配表'].sum() <= self.tax_deduction:
                self.df_08.loc[ind, '其他01'] = self.df_08.loc[ind, '增值税_利润和利润分配表']
            else:
                if self.df_08.loc[self.df_08.index < ind, '增值税_利润和利润分配表'].sum() <= self.tax_deduction:
                    self.df_08.loc[ind, '其他01'] = self.tax_deduction - self.df_08.loc[
                        self.df_08.index < ind, '增值税_利润和利润分配表'].sum()
                else:
                    self.df_08.loc[ind, '其他01'] = 0

        self.df_08['回收固定资产余值'] = self.回收固定资产余值
        self.df_08['回收流动资金'] = self.回收流动资金
        self.df_08['资金来源'] = self.df_08['利润总额'] + self.df_08['折旧费'] + self.df_08['摊销费'] + self.df_08['长期借款'] \
                          + self.df_08['流动资金借款'] + self.df_08['其他短期借款'] + self.df_08['资本金'] \
                          + self.df_08['其他01'] + self.df_08['回收固定资产余值'] + self.df_08['回收流动资金']

        self.df_08['固定资产投资'] = self.建设投资
        self.df_08['建设期利息'] = self.建设期利息
        self.df_08['流动资金'] = self.流动资金
        self.df_08['所得税'] = self.所得税
        self.df_08['应付利润'] = self.应付利润

        self.df_08['本年还本'] = self.本年还本
        self.df_08['偿还流动资金借款本金'] = self.偿还流动资金借款本金
        self.df_08['偿还短期借款本金'] = self.偿还短期借款本金

        self.df_08['借款本金偿还'] = self.df_08['本年还本'] + self.df_08['偿还流动资金借款本金'] + self.df_08['偿还短期借款本金']
        self.df_08['其他02'] = 0

        self.df_08['资金运用'] = self.df_08['固定资产投资'] + self.df_08['建设期利息'] + self.df_08['流动资金'] \
                          + self.df_08['所得税'] + self.df_08['应付利润'] + self.df_08['借款本金偿还'] \
                          + self.df_08['其他02']

        self.df_08['盈余资金（1-2）'] = self.df_08['资金来源'] - self.df_08['资金运用']

        for ind, row in self.df_08.iterrows():
            self.df_08.loc[ind, '累计盈余资金'] = self.df_08.loc[self.df_08.index <= ind, '盈余资金（1-2）'].sum()

        self.df_08 = self.df_08[self.index_name1_08]
        self.df_08 = self.df_08.T
        self.df_08['项目'] = self.df_08.index
        self.df_08['序号'] = self.index_name0_08
        self.df_08.set_index(['序号', '项目'], inplace=True)
        self.df_08 = self.df_08.iloc[:, 1:]
        self.df_08.insert(0, '合计', self.df_08.sum(axis=1))
        return self.df_08

    def cal_df_08(self):

        self.df_08 = self.cal_funds_statement()

        return self.df_08
if __name__ == '__main__':
    # pd.set_option('display.unicode.ambiguous_as_wide', True)
    # pd.set_option('display.unicode.east_asian_width', True)
    # a = FundsStatement()
    # a.cal_profit()
    # # a.cal_balance_sheet()
    # df_08 = a.cal_funds_statement()
    # writer = pd.ExcelWriter('funds_statement.xlsx')
    # df_08.to_excel(writer, float_format='%.5f')
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

    real_08 = FundsStatement(result_01, result_02, result_03, result_04, result_05, result_06,result_07, run_time=1, capacity_mw=50,
                        eleprice=0.29, investment=35000, annual_effective_hours=2800)
    result_08 = real_08.cal_df_08()

    print(result_08.loc[pd.IndexSlice['1.8', '其他01']])