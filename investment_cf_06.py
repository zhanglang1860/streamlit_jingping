#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ZhangWeiguo
@file:investment_cf_06.py
@time:2020/11/27
"""

from financial_plan_cash_flow_05 import *


class InvestmentCF(FinancialPlanCashFlow):
    def default(self):
        InvestmentCF.__init__(self)

    def __init__(self, df_01, df_02, df_03, df_04, df_05, **kargs):
        FinancialPlanCashFlow.__init__(self, df_01, df_02, df_03, df_04, run_time=1, capacity_mw=kargs['capacity_mw'],
                                       eleprice=kargs['eleprice'], investment=kargs['investment'],
                                       annual_effective_hours=kargs['annual_effective_hours'])

        self.df_05_f = df_05
        self.df_05_f['合计'] = 0


        self.资金筹措 = self.df_01_f.loc[pd.IndexSlice['2', '资金筹措']]
        self.流动资金之和 = self.df_01_f.loc[pd.IndexSlice['1.3', '流动资金']].sum()
        self.营业税金附加 = self.df_03_f.loc[pd.IndexSlice['2', '营业税金附加']]
        self.息税前利润 = self.df_03_f.loc[pd.IndexSlice['18', '息税前利润（利润总额+利息支出）']]

        self.columns_name_06 = ['第0年', '第1年', '第2年', '第3年', '第4年', '第5年', '第6年', '第7年', '第8年', '第9年', '第10年', '第11年',
                             '第12年', '第13年', '第14年', '第15年', '第16年', '第17年', '第18年', '第19年', '第20年', '第21年']
        self.index_name0_06 = ['1', '1.1', '1.2', '1.3', '1.4', '2', '2.1', '2.2', '2.3', '2.4', '3', '4', '5', '6', '7','8', '9', '10', '11','12','13',]
        self.index_name1_06 = ['现金流入_投资', '营业收入', '补贴收入', '回收固定资产余值', '回收流动资金', '现金流出_投资', '建设投资',
                            '流动资金', '经营成本',
                            '营业税金附加', '所得税前现金净流量', '累计所得税前净现金流量', '调整所得税', '所得税后净现金流量', '累计所得税后净现金流量']

        self.df = pd.DataFrame(np.zeros(len(self.index_name1_06) * len(self.columns_name_06)).reshape(len(self.columns_name_06),
                                                                                                len(self.index_name1_06)))
        self.df.columns = self.index_name1_06

    # 06项目投资现金流量表

    # 求和函数
    def sum_arry(self, list):
        sum_ = 0
        for i in range(0, len(list)):
            sum_ = sum_ + list[i]
        return sum_

    # 找到第一个正数的i值
    def find_fist_positive(self, fingding):
        find_judge = False
        x_l = 0
        for i in range(0, 21):
            if find_judge == False:
                if fingding[i] <= 0:
                    pass
                else:
                    x_l = i
                    find_judge = True
        return x_l

    # 定义NPV函数（两个定义，默认使用定义2）
    # 定义1 期初发生现金流的NPV
    def npv_f1(self, rate, cashflows):
        total = 0
        for i, cashflow in enumerate(cashflows):
            total += cashflow / (1 + rate / 100) ** i
        return total

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

    # 行序号1-1.4，共5行，现金流入
    # 此处引用03利润和利润分配表-营业收入（self.o_income）、所得税（self.vat），01投资计划与资金筹措表-资金筹措（self.fund_raising）、流动资金（self.wc_sum）
    def investment_cash_flow(self):

        self.df.loc[21, '回收固定资产余值'] = (self.资金筹措.iloc[0] - self.tax_deduction) * self.residual_rate
        self.df.loc[21, '回收流动资金'] = self.流动资金之和
        for i in range(1, 22):
            # ?一样的条目需要如何引用
            self.df.loc[i, '营业收入'] = self.营业收入.iloc[i]
            if self.增值税.iloc[0:i + 1].sum() <= self.tax_deduction:
                self.df.loc[i, '补贴收入'] = self.增值税.iloc[i]
            elif self.增值税.iloc[0:i + 1].sum() - self.tax_deduction < self.增值税.iloc[i]:
                self.df.loc[i, '补贴收入'] = self.增值税.iloc[i] - (self.增值税.iloc[0:i + 1].sum() - self.tax_deduction) / 2
            else:
                self.df.loc[i, '补贴收入'] = self.增值税.iloc[i] / 2
            self.df.loc[i, '现金流入_投资'] = self.df.loc[i, '营业收入'] + self.df.loc[i, '补贴收入'] + self.df.loc[i, '回收固定资产余值'] + \
                                        self.df.loc[i, '回收流动资金']


        # 行序号2-2.4，共5行，现金流出
        # def cash_outflow(self):
        # 引用01投资计划与资金筹措表-建设投资(self.constr_invest)、流动资金（self.wc），02总成本费用表-经营成本(self.o_cost)、03利润和利润分配表-营业税金及附加(self.tax_sur)(Business Taxes and Surcharges)
        self.df.loc[1, '建设投资'] = self.建设投资.iloc[1]
        self.df.loc[2, '流动资金'] = self.流动资金.iloc[2]
        for i in range(1, 22):
            self.df.loc[i, '经营成本'] = self.经营成本.iloc[i]
            self.df.loc[i, '营业税金附加'] = self.营业税金附加.iloc[i]
            self.df.loc[i, '现金流出_投资'] = self.df.loc[i, '建设投资'] + self.df.loc[i, '流动资金'] + self.df.loc[i, '经营成本'] + \
                                        self.df.loc[i, '营业税金附加']
        # self.cash_outflow_sum = self.sum_arry(self.cash_outflow_value)
        # self.constr_investment_sum = self.sum_arry(self.constr_investment)
        # self.working_capital_sum = self.sum_arry(self.working_capital)
        # self.operating_cost_sum = self.sum_arry(self.operating_cost)
        # self.tax_surcharge_sum = self.sum_arry(self.tax_surcharge)
        # return self.df.T
        # cash_outflow_value, self.constr_investment, self.working_capital, self.operating_cost, self.tax_surcharge
        # , self.cash_outflow_sum, self.constr_investment_sum, self.working_capital_sum, self.operating_cost_sum, self.tax_surcharge_sum

        # 行序号3-7，共5行，净现金流量
        # def ncf(self):
        # 此处引用现金流入、现金流出，03利润和利润分配表-息税前利润（self.ebit）
        for i in range(1, 22):

            self.df.loc[i, '所得税前现金净流量'] = self.df.loc[i, '现金流入_投资'] - self.df.loc[i, '现金流出_投资']
            self.df.loc[i, '累计所得税前净现金流量'] = self.df.loc[1:i + 1, '所得税前现金净流量'].sum()
            if i > 1:
                if i < (2 + self.free):
                    self.df.loc[i, '调整所得税'] = 0
                elif i < (2 + self.free + self.halved):
                    self.df.loc[i, '调整所得税'] = self.息税前利润.iloc[i] * self.it_rate / 100 / 2
                else:
                    self.df.loc[i, '调整所得税'] = self.息税前利润.iloc[i] * self.it_rate / 100
            self.df.loc[i, '所得税后净现金流量'] = self.df.loc[i, '所得税前现金净流量'] - self.df.loc[i, '调整所得税']
            self.df.loc[i, '累计所得税后净现金流量'] = self.df.loc[1:i + 1, '所得税后净现金流量'].sum()

            # 计算指标 NPV
            # pv_investment_bef = self.ncf_before[i] / ((1 + self.br_industry_before) ** i)
            # npv_investment_bef = self.sum_arry(pv_investment_bef)
            # pv_investment_aft = self.ncf_after[i] / ((1 + self.br_industry_after) ** i)
            # npv_investment_aft = self.sum_arry(pv_investment_aft)
        # 计算指标 NPV
        self.df.loc[1, '项目投资财务净现值（所得税前）'] = self.npv_f(self.br_industry_before / 100, self.df.loc[1:, '所得税前现金净流量'])
        self.df.loc[1, '项目投资财务净现值（所得税后）'] = self.npv_f(self.br_industry_after / 100, self.df.loc[1:, '所得税后净现金流量'])
        # self.ncf_before_sum = self.sum_arry(self.df.loc['所得税前现金净流量'])
        # self.incometax_adjust_sum = self.sum_arry(self.df.loc['调整所得税'])
        # self.ncf_after_sum = self.sum_arry(self.df.loc['所得税后净现金流量'])
        # 计算指标 PBP 项目投资回收期（所得税前与税后）
        m_bef = self.find_fist_positive(self.df.loc[:, '累计所得税前净现金流量'])
        self.df.loc[1, '项目投资回收期（所得税前）'] = m_bef - self.df.loc[m_bef, '累计所得税前净现金流量'] / self.df.loc[m_bef, '所得税前现金净流量']
        m_aft = self.find_fist_positive(self.df.loc[:, '累计所得税后净现金流量'])
        self.df.loc[1, '项目投资回收期（所得税后）'] = m_aft - self.df.loc[m_aft, '累计所得税后净现金流量'] / self.df.loc[m_aft, '所得税后净现金流量']

        # print("X"*10)
        # print(m_bef,m_bef)
        # 计算指标 IRR


        self.df.loc[1, '项目投资财务内部收益率（所得税前）'] = self.irr_f(self.df.loc[:, '所得税前现金净流量'])
        self.df.loc[1, '项目投资财务内部收益率（所得税后）'] = self.irr_f(self.df.loc[:, '所得税后净现金流量'])

        self.df = self.df.T
        self.df.insert(0, '合计', self.df.sum(axis=1))
        return self.df

        # return self.df.T
        # ncf_before, self.ncf_before_accum, self.incometax_adjust, self.ncf_after, self.ncf_after_accum, self.ncf_before_sum, self.incometax_adjust_sum, self.ncf_after_sum, \
        # self.npv_investment_bef, self.npv_investment_aft, payback_period_bef, payback_period_aft, self.irr_investment_bef, self.irr_investment_aft


    def cal_df_06(self):

        self.df_06 = self.investment_cash_flow()

        self.df_06['项目'] = self.df_06.index
        self.df_06['序号'] = self.index_name0_06
        self.df_06.set_index(['序号', '项目'], inplace=True)
        self.df_06=self.df_06.fillna(0)
        self.df_06=self.df_06.drop(columns=self.df_06.columns[1],axis=1)

        return self.df_06

if __name__ == '__main__':
    # a = CostParameters()
    # self.default()
    # print(zz_sum)

    # a = investment_cf()
    # xxx = a.investment_cash_flow()
    # # xxx = a.cash_outflow()
    # # xxx = a.ncf()
    # df = xxx
    # print(df)
    #
    # writer = pd.ExcelWriter('investment_cf_06.xlsx')
    # df.to_excel(writer, float_format='%.5f')
    # writer.save()

    # qq = [-35000.00, 3292.10, 3442.10, 3442.10, 3284.60, 3284.60, 3284.60, 3284.60, 3147.35, 2856.19, 2856.19, 2856.19,
    #       2856.19, 2856.19, 2856.19, 2856.19, 2698.69, 2698.69, 2698.69, 2698.69, 2848.69]
    # hh = [-35000.00, 3292.10, 3442.10, 3442.10, 3156.86, 3156.86, 3156.86, 3029.12, 2867.03, 2591.05, 2591.05, 2591.05,
    #       2591.05, 2591.05, 2591.05, 2591.05, 2472.93, 2472.93, 2472.93, 2024.02, 2174.02]
    # tt = [-35000.0, 3292.1, 3442.1, 3442.1, 3156.8624999999997, 3156.8624999999997, 3156.8624999999997, 3029.125,
    #       2867.0275, 2590.5075, 2590.5075, 2590.5075, 2590.5075, 2590.5075, 2590.5075, 2590.5075, 2472.3825, 2472.3825,
    #       2472.3825, 2023.4775, 2173.4775]
    # npv_t = a.npv_f(0.07, tt)
    # print(npv_t)
    # npv_q = a.npv_f(0.08, qq)
    #
    # npv_h = a.npv_f(0.07, hh)
    #
    # print(npv_q, npv_h)

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
    #
    print(result_06.iloc[:, :4])
