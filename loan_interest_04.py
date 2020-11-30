#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ZhangWeiguo
@file:loan_interest_04.py
@time:2020/11/25
"""
from profit_table_03 import *


# 04借款还本付息计划表
class LoanInterest(ProfitTable):
    def default(self):
        LoanInterest.__init__(self)

    def __init__(self, df_01, df_02, df_03, **kargs):
        ProfitTable.__init__(self, df_01, df_02, run_time=1, capacity_mw=kargs['capacity_mw'],
                             eleprice=kargs['eleprice'], investment=kargs['investment'],
                             annual_effective_hours=kargs['annual_effective_hours'])

        self.df_03_f = df_03
        self.df_03_f['合计'] = 0

        # print(self.df_01_f.loc[pd.IndexSlice['2.2.1','长期借款'],:])
        # self.长期借款 = [0, 28656.92, 0.00]  # 01投资计划与资金筹措表-长期借款（self.long_loan_b）
        self.长期借款 = self.df_01_f.loc[pd.IndexSlice['2.2.1', '长期借款']]
        self.流动资金借款 = self.df_01_f.loc[pd.IndexSlice['2.2.2', '流动资金借款']]
        # self.营业收入 = [0, 0.00, 3592.92, 3592.92, 3592.92, 3592.92, 3592.92, 3592.92, 3592.92, 3592.92, 3592.92, 3592.92,
        #              3592.92, 3592.92, 3592.92, 3592.92, 3592.92, 3592.92, 3592.92, 3592.92, 3592.92,
        #              3592.92]  # 03利润和利润分配表-营业收入(self.o_income)
        self.营业收入 = self.df_03_f.loc[pd.IndexSlice['1', '营业收入']]

        # self.增值税 = [0, 0.00, 467.08, 467.08, 467.08, 467.08, 467.08, 467.08, 467.08, 467.08, 467.08, 467.08, 467.08,
        #             467.08, 467.08, 467.08, 467.08, 467.08, 467.08, 467.08, 467.08, 467.08]  # 03利润和利润分配表-增值税(self.vat)
        self.增值税 = self.df_03_f.loc[pd.IndexSlice['20', '增值税']]
        # self.经营成本 = [0, 0.00, 617.90, 617.90, 617.90, 775.40, 775.40, 775.40, 775.40, 775.40, 932.90, 932.90, 932.90,
        #              932.90, 932.90, 932.90, 932.90, 1090.40, 1090.40, 1090.40, 1090.40,
        #              1090.40]  # 02总成本费用表-经营成本(self.o_cost)
        self.经营成本 = self.df_02_f.loc[pd.IndexSlice['12', '经营成本']]
        # self.息税前利润 = [0, 0.00, 1179.40, 1179.40, 1179.40, 1021.90, 1021.90, 1021.90, 1021.90, 1121.29, 1060.57, 1060.57,
        #               1060.57, 1060.57, 1060.57, 1060.57, 1060.57, 903.07, 903.07, 903.07, 2698.69,
        #               2698.69]  # 03利润和利润分配表-息税前利润(self.ebit)
        self.息税前利润 = self.df_03_f.loc[pd.IndexSlice['18', '息税前利润（利润总额+利息支出）']]

        # self.息税折旧摊销前利润 = [0, 0.00, 2975.02, 2975.02, 2975.02, 2817.52, 2817.52, 2817.52, 2817.52, 2916.91, 2856.19,
        #                   2856.19,
        #                   2856.19, 2856.19, 2856.19, 2856.19, 2856.19, 2698.69, 2698.69, 2698.69, 2698.69,
        #                   2698.69]  # 03利润和利润分配表-息税折旧摊销前利润(self.ebitda)

        self.息税折旧摊销前利润 = self.df_03_f.loc[pd.IndexSlice['19', '息税折旧摊销前利润']]

        # self.所得税 = [0, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 10.28, 122.84, 151.02, 179.20,
        #             207.38, 235.56, 224.36, 224.36, 224.36, 673.27, 673.27]  # 03利润和利润分配表-所得税(self.income_tax)
        self.所得税 = self.df_03_f.loc[pd.IndexSlice['8', '所得税']]

        self.columns_name = ['第0年', '第1年', '第2年', '第3年', '第4年', '第5年', '第6年', '第7年', '第8年', '第9年', '第10年', '第11年',
                             '第12年', '第13年', '第14年', '第15年', '第16年', '第17年', '第18年', '第19年', '第20年', '第21年']
        self.index_name0 = ['1', '1.1', '1.2', '1.2.1', '1.2.2', '1.3', '2', '2.1', '2.2','2.3', '3', '3.1', '3.2', '3.3',
                            '3.4','3.5']
        self.index_name1 = ['长期借款', '年初借款余额', '当期还本付息', '本年还本', '本年付息', '期末借款余额', '流动资金借款', '流动资金借款累计', '流动资金利息',
                            '偿还流动资金借款本金', '短期借款', '偿还短期借款本金', '短期借款利息', '利息备付率', '偿债备付率','利息支出']
        self.df = pd.DataFrame(
            np.zeros(len(self.index_name1) * len(self.columns_name)).reshape(
                (len(self.index_name1), len(self.columns_name))))
        self.df = self.df.T
        self.df.columns = self.index_name1

    # 求和函数
    def sum_arry(self, list):
        sum_ = 0
        for i in range(0, len(list)):
            sum_ = sum_ + list[i]
        return sum_

    # 行序号1-1.3，共6行，长期借款
    def long_loan(self):

        # 调用投资计划与资金筹措表，得到长期借款第一年数额
        self.df.loc[1, '长期借款'] = self.长期借款[1]
        self.df.loc[2, '年初借款余额'] = self.df.loc[1, '长期借款']

        for i in range(2, 22):
            if i < (self.scheduled_repayment + 2):
                self.df.loc[i, '本年还本'] = self.df.loc[2, '年初借款余额'] / self.scheduled_repayment
            else:
                self.df.loc[i, '本年还本'] = 0
            self.df.loc[i, '期末借款余额'] = self.df.loc[i, '年初借款余额'] - self.df.loc[i, '本年还本']

            if i < 21:
                self.df.loc[i + 1, '年初借款余额'] = self.df.loc[i, '期末借款余额']

            self.df.loc[i, '本年付息'] = self.df.loc[i, '年初借款余额'] * self.long_loan_rate / 100
            self.df.loc[i, '当期还本付息'] = self.df.loc[i, '本年还本'] + self.df.loc[i, '本年付息']
        # self.long_loan_sum = self.sum_arry(self.long_loan_principal)
        # self.debt_service_sum = self.sum_arry(self.debt_service)
        # self.repay_principal_sum = self.sum_arry(self.repay_principal)
        # self.repay_int_sum = self.sum_arry(self.repay_int)
        # self.df = self.df.T
        return self.df.T
        # ['长期借款'], self.df['年初借款余额'], self.df['当期还本付息'], self.df['本年还本'], self.df['本年付息'], self.df[
        #     '期末借款余额']
        # self.long_loan_sum, self.debt_service_sum, self.repay_principal_sum, self.repay_int_sum

    # 行序号2-2.3，共4行，流动资金借款
    # 调用01投资计划与资金筹措表-流动资金借款
    def wc_loan(self):
        self.df.loc[2, '流动资金借款'] = self.流动资金借款[2]
        for i in range(1, 22):
            if i > 1:
                self.df.loc[i, '流动资金借款累计'] = self.df.loc[1:i + 1, '流动资金借款'].sum() - self.df.loc[1:i, '偿还流动资金借款本金'].sum()

            self.df.loc[i, '流动资金利息'] = self.df.loc[i, '流动资金借款累计'] * self.liquidity_loan_rate / 100
        self.df.loc[21, '偿还流动资金借款本金'] = self.df.loc[21, '流动资金借款累计']
        # self.wc_loan_sum = self.sum_arry(self.wc_loan_principal)
        # self.wc_int_sum = self.sum_arry(self.wc_loan_int)
        # self.repay_wc_sum = self.sum_arry(self.repay_wc_principal)
        # self.df=self.df.T
        return self.df.T
        # ['流动资金借款'], self.df['流动资金借款累计'], self.df['流动资金利息'], self.df['偿还流动资金借款本金']
        # , self.wc_loan_sum, self.wc_int_sum, self.repay_wc_sum

    # 行序号3-3.2，共3行,短期借款
    # 计算此项目时，需要用到营业收入和增值税（03利润和利润分配表），经营成本（02总成本费用表）
    def short_loan(self):
        for i in range(1, 22):
            if i > 0:
                if self.营业收入[i] + self.增值税[i] - self.df.loc[i, '本年还本'] - self.df.loc[i, '本年付息'] - self.df.loc[
                    i, '流动资金利息'] - self.经营成本[i] - self.df.loc[i - 1, '短期借款'] < 0:
                    self.df.loc[i, '短期借款'] = -(
                            self.营业收入[i] + self.增值税[i] - self.df.loc[i, '本年还本'] - self.df.loc[i, '本年付息'] -
                            self.df.loc[i, '流动资金利息'] - self.经营成本[i] - self.df.loc[i - 1, '短期借款']) / (
                                                     1 - self.short_loan_rate / 100)
                else:
                    self.df.loc[i, '短期借款'] = 0
                self.df.loc[i, '偿还短期借款本金'] = self.df.loc[i - 1, '短期借款']
            self.df.loc[i, '短期借款利息'] = self.df.loc[i, '短期借款'] * self.short_loan_rate / 100
        # short_loan_sum = self.sum_arry(self.short_loan_principal)
        # repay_short_sum = self.sum_arry(self.repay_short_principal)
        # short_int_sum = self.sum_arry(self.short_int)
        # self.df = self.df.T

        return self.df.T
        # ['短期借款'], self.df['偿还短期借款本金'], self.df['短期借款利息']
        # , short_loan_sum, repay_short_sum, short_int_sum

    # 计算利息支出，用于02总成本费用表
    def int_expense(self):
        for i in range(1, 22):
            self.df.loc[i, '利息支出'] = self.df.loc[i, '本年付息'] + self.df.loc[i, '流动资金利息'] + self.df.loc[i, '短期借款利息']
        # int_expense_sum = self.sum_arry(self.int_expense_all)
        # self.df = self.df.T
        return self.df.T
        # ['利息支出']
        # , int_expense_sum

    # 计算两个指标，利息备付率（利息保障倍数（Interest Protection Multiples）ICR）、偿债备付率(Debt Coverage Ratio，DCR)
    # 需要用到03利润和利润分配表ebit，ebitda，income_tax
    def coverage_ratio(self):

        for i in range(1, 22):
            # 注意此处0.0001的使用，实际应该是0
            if self.df.loc[i, '本年付息'] > 0.0001:
                self.df.loc[i, '利息备付率'] = self.息税前利润[i] / (self.df.loc[i, '本年付息'] + self.df.loc[i, '流动资金利息'])
                self.df.loc[i, '偿债备付率'] = (self.息税折旧摊销前利润[i] - self.所得税[i]) / (
                        self.df.loc[i, '当期还本付息'] + self.df.loc[i, '流动资金利息'] + self.df.loc[i, '偿还流动资金借款本金'])
            else:
                self.df.loc[i, '利息备付率'] = 0
                self.df.loc[i, '偿债备付率'] = 0
        self.df = self.df.T
        self.df.insert(0, '合计', self.df.sum(axis=1))
        return self.df

    def cal_df_04(self):

        self.df_04 = self.long_loan()
        self.df_04 = self.wc_loan()
        self.df_04 = self.short_loan()
        self.df_04 = self.int_expense()
        self.df_04 = self.coverage_ratio()

        # self.df_04=self.df_04.drop('利息支出',axis=0)
        self.df_04['项目'] = self.df_04.index
        self.df_04['序号'] = self.index_name0
        self.df_04.set_index(['序号', '项目'], inplace=True)

        self.df_04=self.df_04.drop(columns=self.df_04.columns[1],axis=1)

        return self.df_04


if __name__ == '__main__':
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd.set_option('display.unicode.east_asian_width', True)

    # real_01 = InvestmentFinancing()
    # result_01 = real_01.cal_df_01(capacity_mw=50, eleprice=0.29, investment=45000, annual_effective_hours=2800)
    # a = LoanInterest(result_01)
    # result_04 = a.cal_df_04()

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
    print(result_04.iloc[:,0:3])

    #
    # writer = pd.ExcelWriter('LoanInterest.xlsx')
    # df.to_excel(writer, float_format='%.5f')
    # writer.save()
