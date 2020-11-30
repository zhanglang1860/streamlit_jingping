#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ZhangWeiguo
@file:capital_cf_07.py
@time:2020/11/27
"""

from investment_cf_06 import *


class CapitalCF(InvestmentCF):
    def default(self):
        CapitalCF.__init__(self)

    def __init__(self, df_01, df_02, df_03, df_04, df_05, df_06, **kargs):
        InvestmentCF.__init__(self, df_01, df_02, df_03, df_04, df_05, run_time=1, capacity_mw=kargs['capacity_mw'],
                              eleprice=kargs['eleprice'], investment=kargs['investment'],
                              annual_effective_hours=kargs['annual_effective_hours'])
        self.df_06_f = df_06
        self.df_06_f['合计'] = 0

        # 调用数据

        self.补贴收入 = self.df_06_f.loc[pd.IndexSlice['1.2', '补贴收入']]
        self.回收固定资产余值 = self.df_06_f.loc[pd.IndexSlice['1.3', '回收固定资产余值']]
        self.回收流动资金 = self.df_06_f.loc[pd.IndexSlice['1.4', '回收流动资金']]
        self.本年还本 = self.df_04_f.loc[pd.IndexSlice['1.2.1', '本年还本']]
        self.偿还流动资金借款本金 = self.df_04_f.loc[pd.IndexSlice['2.3', '偿还流动资金借款本金']]
        self.所得税 = self.df_03_f.loc[pd.IndexSlice['8', '所得税']]

        self.columns_name = ['第0年', '第1年', '第2年', '第3年', '第4年', '第5年', '第6年', '第7年', '第8年', '第9年', '第10年', '第11年',
                             '第12年', '第13年', '第14年', '第15年', '第16年', '第17年', '第18年', '第19年', '第20年', '第21年']
        self.index_name0_07 = ['1', '1.1', '1.2', '1.3', '1.4', '2', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '3', '4',
                               '5']
        self.index_name1 = ['现金流入', '营业收入', '补贴收入', '回收固定资产余值', '回收流动资金', '现金流出', '项目资本金',
                            '借款本金偿还', '借款利息支付', '经营成本',
                            '营业税金附加', '所得税', '净现金流量']
        self.df = pd.DataFrame(np.zeros(len(self.index_name1) * len(self.columns_name)).reshape(len(self.columns_name),
                                                                                                len(self.index_name1)))
        self.df.columns = self.index_name1

    # 定义求和函数sum
    def sum_arry(self, list):
        sum_ = 0
        for i in range(0, len(list)):
            sum_ += list[i]
        return sum_

    # 定义2 期末发生现金流的NPV
    def npv_f(self, rate, cashflows):
        total = 0
        for i, cashflow in enumerate(cashflows):
            total += cashflow / (1 + rate) ** (i + 1)
        return total

    # 定义IRR函数(需要和sum_arry()与npv_f()结合使用
    def irr_f(self, cashflows, interations=100):
        if len(cashflows) == 0:
            print('number of cash flows is zero')
            return None
        else:
            tmp = [1 if each >= 0 else 0 for each in cashflows]
            if tmp.count(1) == 0 or tmp.count(0) == 0:
                print("全大于等于0，或全小于0")
                return None
            else:
                rate = 0.1
                minDistance = 1e-15
                wasHi = False
                if self.sum_arry(cashflows) >= 0:
                    irr = rate
                else:
                    rate = 0.5
                    irr = -1 * rate
                investment = cashflows[0]
                for i in range(1, interations + 1):
                    npv = self.npv_f(irr, cashflows)
                    if abs(npv) <= 0.0001:
                        return irr
                    if npv > 0:
                        if wasHi == True:
                            rate = rate / 2
                        irr = irr + rate
                        if wasHi == True:
                            rate -= minDistance
                            wasHi = False

                    if npv < 0:
                        rate = rate / 2
                        irr = irr - rate
                        wasHi = True

                    if rate <= minDistance:
                        return irr

    # 序号1-1.4，共5行，现金流入；序号2-2.6，共7行，现金流出；序号3净现金流量
    # 需要引用
    # 01投资计划与资金筹措表-资本金(self.capital_)
    # 02总成本费用表-经营成本(self.o_cost)
    # 03利润和利润分配表-营业收入（self.o_income）,营业税金及附加(self.tax_sur)
    # 04借款还本付息计划表-本年还本（self.repay_long_loan）,偿还流动资金借款本金（self.repay_wc_loan）,利息支出（self.int_expense）
    # 06项目投资现金流量表-补贴收入(self.subsidy_income)、回收固定资产余值(self.recovery_residual_fa)、回收流动资金(self.recovery_wc)、
    def cashflow(self):
        # 序号1-1.4，共5行，现金流入
        for i in range(1, 22):
            self.df.loc[i, '营业收入'] = self.营业收入[i]
            self.df.loc[i, '补贴收入'] = self.补贴收入[i]
            self.df.loc[i, '回收固定资产余值'] = self.回收固定资产余值[i]
            self.df.loc[i, '回收流动资金'] = self.回收流动资金[i]
            self.df.loc[i, '现金流入'] = self.df.loc[i, '营业收入'] + self.df.loc[i, '补贴收入'] + self.df.loc[i, '回收固定资产余值'] + \
                                     self.df.loc[i, '回收流动资金']
        # self.revenue_sum = self.sum_arry(self.revenue)
        # self.subsidy_sum = self.sum_arry(self.subsidy)
        # self.recovery_residual_sum = self.sum_arry(self.recovery_residual)
        # self.recovery_wc_a_sum = self.sum_arry(self.recovery_wc_a)
        # self.in_cf_sum = self.sum_arry(self.in_cf)
        # return self.df.T

        # 序号2-2.6，共7行，现金流出
        for i in range(1, 22):
            self.df.loc[i, '项目资本金'] = self.资本金_投资计划与资金筹措表.iloc[i]
            self.df.loc[i, '借款本金偿还'] = self.本年还本[i] + self.偿还流动资金借款本金[i]
            self.df.loc[i, '借款利息支付'] = self.利息支出[i]
            self.df.loc[i, '经营成本'] = self.经营成本[i]
            self.df.loc[i, '营业税金附加'] = self.营业税金附加.iloc[i]
            self.df.loc[i, '所得税'] = self.所得税[i]
            self.df.loc[i, '现金流出'] = self.df.loc[i, '项目资本金'] + self.df.loc[i, '借款本金偿还'] + self.df.loc[i, '借款利息支付'] + \
                                     self.df.loc[i, '经营成本'] + \
                                     self.df.loc[i, '营业税金附加'] + self.df.loc[i, '所得税']
        # self.out_cf_sum = self.sum_arry(self.out_cf)
        # self.capital_sum = self.sum_arry(self.capital)
        # self.repay_principal_sum = self.sum_arry(self.repay_principal)
        # self.repay_int_sum = self.sum_arry(self.repay_int)
        # self.operating_cost_sum = self.sum_arry(self.operating_cost)
        # self.tax_surcharge_sum = self.sum_arry(self.tax_surcharge)
        # self.income_tax_sum = self.sum_arry(self.income_tax)
        # return self.df.T

        # def aaa(self):
        # 序号3净现金流量
        for i in range(1, 22):
            self.df.loc[i, '净现金流量'] = self.df.loc[i, '现金流入'] - self.df.loc[i, '现金流出']

        # self.net_cf_sum = self.sum_arry(self.net_cf)
        # 计算指标 IRR
        self.df.loc[1, '资本金财务内部收益率'] = self.irr_f(self.df.loc[:, '净现金流量'])
        # 计算指标NPV
        self.df.loc[1, '资本金财务净现值'] = self.npv_f(self.br_capital / 100, self.df.loc[1:, '净现金流量'])

        self.df = self.df.T
        self.df.insert(0, '合计', self.df.sum(axis=1))
        return self.df

    # return self.in_cf, self.in_cf_sum, self.revenue, self.revenue_sum, self.subsidy, self.subsidy_sum, \
    #        self.recovery_residual, self.recovery_residual_sum, self.recovery_wc_a, self.recovery_wc_a_sum, \
    #        self.out_cf, self.out_cf_sum, self.capital, self.capital_sum, self.repay_principal, self.repay_principal_sum, \
    #        self.repay_int, self.repay_int_sum, self.operating_cost, self.operating_cost_sum, self.tax_surcharge, self.tax_surcharge_sum, \
    #        self.income_tax, self.income_tax_sum, self.net_cf, self.net_cf_sum,self.irr_net_cf,self.npv_net_cf

    def cal_df_07(self):

        self.df_07 = self.cashflow()

        self.df_07['项目'] = self.df_07.index
        self.df_07['序号'] = self.index_name0_07
        self.df_07.set_index(['序号', '项目'], inplace=True)
        self.df_07 = self.df_07.fillna(0)
        self.df_07 = self.df_07.drop(columns=self.df_07.columns[1], axis=1)

        return self.df_07


if __name__ == '__main__':
    # a = capital_cf()
    # xxx = a.cashflow()
    # df = xxx
    # # ncf = [-7164.23, -219.05000000000018, -64.80000000000018, 50.629999999999654, 6.179999999999836, 125.61000000000013,
    # #        241.3499999999999, 354.0699999999997, 329.5300000000002, 151.09000000000015, 253.52999999999975,
    # #        253.69000000000005, 338.22000000000025, 422.7600000000002, 507.2999999999997, 591.8400000000001, 2468.71,
    # #        2468.71, 2468.71, 2019.8000000000002, 2064.8]
    # # yyy = a.npv_f(8 / 100, ncf)
    # print(df)
    #
    # writer = pd.ExcelWriter('capital_cf_07.xlsx')
    # df.to_excel(writer, float_format='%.5f')
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

    print(result_07)