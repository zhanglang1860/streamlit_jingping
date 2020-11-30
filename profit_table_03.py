#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Zhangyicheng
@file:profit_table_03.py
@time:2020/11/11
"""

from total_cost_02 import *


class ProfitTable(TotalCost):
    def default(self):
        ProfitTable.__init__(self)

    def __init__(self, df_01, df_02, **kargs):
        TotalCost.__init__(self, df_01, run_time=1, capacity_mw=kargs['capacity_mw'], eleprice=kargs['eleprice'],
                           investment=kargs['investment'], annual_effective_hours=kargs['annual_effective_hours'])

        self.df_02_f = df_02
        self.df_02_f['合计'] = 0

        # self.资本金_投资计划与资金筹措表 = [0, 7164.23, 45.00, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.资本金_投资计划与资金筹措表 = self.df_01_f.loc[pd.IndexSlice['2.1', '资本金（资金筹措）']]
        # self.利息支出 = [0.00, 0.00, 1705.69, 1596.44, 1481.01, 1367.96, 1248.53, 1132.79, 1020.07, 907.36, 794.64, 681.92,
        #              569.20, 456.49, 343.77, 231.05, 118.33, 5.62, 5.62, 5.62, 5.62, 5.62]
        self.利息支出 = self.df_02_f.loc[pd.IndexSlice['7', '利息支出']]

        # self.折旧费 = [0.00, 0.00, 1795.62, 1795.62, 1795.62, 1795.62, 1795.62, 1795.62, 1795.62, 1795.62, 1795.62,
        #             1795.62, 1795.62, 1795.62, 1795.62, 1795.62, 1795.62, 1795.62, 1795.62, 1795.62, 0.00, 0.00]
        self.折旧费 = self.df_02_f.loc[pd.IndexSlice['1', '折旧费']]

        self.ongrid_t = [0 for i in range(0, 22)]  # 上网电量
        self.price_notax_t = [0 for i in range(0, 22)]  # 电价（不含增值税）（元/kWh）
        self.price_tax_t = [self.eleprice for i in range(0, 22)]  # 电价（含增值税）（元/kWh）
        self.operating_income_t = [0 for i in range(0, 22)]  # 营业收入

        self.business_tax_surcharge_t = [0 for i in range(0, 22)]  # 营业税金附加
        self.urban_maintenance_tax_t = [0 for i in range(0, 22)]  # 城市维护建设税
        self.education_surcharge_t = [0 for i in range(0, 22)]  # 教育费附加
        self.vat_t = [0 for i in range(0, 22)]  # 增值税

        # self.total_cost = [0.00, 0.00, 4119.21, 4009.96, 3894.53, 3938.98, 3819.55, 3703.81, 3591.09, 3478.38, 3523.16,
        #                    3410.44, 3297.72, 3185.01, 3072.29, 2959.57, 2846.85, 2891.64, 2891.64, 2891.64, 1096.02,
        #                    1096.02]  # 总成本费用
        self.total_cost = self.df_02_f.loc[pd.IndexSlice['11', '总成本费用']]

        # print("SSSSSSSSS")
        # print(self.折旧费)
        # print(self.total_cost)

        self.subsidy_income_taxable_t = [0 for i in range(0, 22)]  # 补贴收入（应税）
        self.total_profit_t = [0 for i in range(0, 22)]  # 利润总额（1-2-3+4）
        self.offset_prior_losses_t = [0 for i in range(0, 22)]  # 弥补以前年度亏损
        self.taxable_income_t = [0 for i in range(0, 22)]  # 应纳税所得额（5-6）
        self.income_tax_t = [0 for i in range(0, 22)]  # 所得税
        self.subsidy_income_notax_t = [0 for i in range(0, 22)]  # 补贴收入（免税）
        self.net_profit_t = [0 for i in range(0, 22)]  # 净利润（5-8+9）

        self.undistributed_profit_f_t = [0 for i in range(0, 22)]  # 期初未分配的利润
        self.statutory_surplus_reserve_t = [0 for i in range(0, 22)]  # 提取法定盈余公积金
        self.profit_payable_t = [0 for i in range(0, 22)]  # 应付利润
        self.distributed_profit_t = [0 for i in range(0, 22)]  # 可供分配的利润（10+11）
        self.profits_available_investor_t = [0 for i in range(0, 22)]  # 可供投资者分配的利润（12-13）
        self.surplus_reserve_fund_t = [0 for i in range(0, 22)]  # 提取任意盈余公积金
        self.undistributed_profit_t = [0 for i in range(0, 22)]  # 未分配利润（14-15-16）
        self.edit = [0 for i in range(0, 22)]  # 息税前利润（利润总额+利息支出）
        self.earnings_before_interest = [0 for i in range(0, 22)]  # 息税折旧摊销前利润
        #

        self.columns_name_03 = ['第0年', '第1年', '第2年', '第3年', '第4年', '第5年', '第6年', '第7年', '第8年', '第9年', '第10年',
                                '第11年', '第12年', '第13年', '第14年', '第15年', '第16年', '第17年', '第18年', '第19年',
                                '第20年', '第21年']

        self.index_name0_03 = ['0', '0.1', '0.2', '1', '2', '2.1', '2.2', '3', '4', '5', '6', '7', '8', '9',
                               '10', '11', '12', '13', '14', '15', '16', '17', '18', '19','20' ]

        self.index_name1_03 = ['上网电量（MWh）', '电价（不含增值税）（元/kWh）', '电价（含增值税）（元/kWh）',
                               '营业收入', '营业税金附加', '城市维护建设税', '教育费附加',
                               '总成本费用', '补贴收入（应税）', '利润总额（1-2-3+4）', '弥补以前年度亏损',
                               '应纳税所得额（5-6）', '所得税', '补贴收入（免税）', '净利润（5-8+9）',
                               '期初未分配的利润', '可供分配的利润（10+11）', '提取法定盈余公积金', '可供投资者分配的利润（12-13）',
                               '提取任意盈余公积金', '应付利润', '未分配利润（14-15-16）', '息税前利润（利润总额+利息支出）',
                               '息税折旧摊销前利润', '增值税']

        self.df_03 = pd.DataFrame(
            np.zeros(len(self.index_name1_03) * len(self.columns_name_03)).reshape(
                (len(self.index_name1_03), len(self.columns_name_03))))
        self.df_03 = self.df_03.T
        self.df_03.columns = self.index_name1_03

        self.result = [self.ongrid_t, self.price_notax_t, self.price_tax_t, self.operating_income_t,
                       self.business_tax_surcharge_t, self.urban_maintenance_tax_t, self.education_surcharge_t,
                       self.total_cost, self.subsidy_income_taxable_t, self.total_profit_t, self.offset_prior_losses_t,
                       self.taxable_income_t, self.income_tax_t, self.subsidy_income_notax_t, self.net_profit_t,
                       self.undistributed_profit_f_t, self.distributed_profit_t, self.statutory_surplus_reserve_t,
                       self.profits_available_investor_t, self.surplus_reserve_fund_t, self.profit_payable_t,
                       self.undistributed_profit_t, self.edit, self.earnings_before_interest,self.vat_t]

        self.df_03_f = self.arry_dic(self.result,  self.index_name1_03,self.index_name0_03)


    @classmethod
    def sum_arry(cls, list):
        sum_ = 0
        for i in range(0, len(list)):
            sum_ = sum_ + list[i]
        return sum_

    def cal_losses_pre_years(self, years):
        losses_pre_years = 0
        profit = False
        # 取出当前列的下三角矩阵的列数
        year_final = years
        df = pd.DataFrame(np.zeros((years + 1) ** 2).reshape(years + 1, years + 1))
        # 计算之前矩阵
        for year in range(2, year_final + 1):
            for i in range(2, year + 1):
                if i < year:
                    # 复制上一步的下三角数值
                    df.at[year, i] = df.at[year - 1, i]
                else:
                    # 最后一个取当年利润
                    df.at[year, i] = self.total_profit_t[year]

            if year < 7:
                # '若当年利润大于0 且前6年时
                if self.total_profit_t[year] > 0:
                    # '进行逐年抵扣
                    for j in range(2, year):
                        if j == 2:
                            df.at[year, j] = df.at[year, j] + self.total_profit_t[year]
                        else:
                            df.at[year, j] = df.at[year, j] + df.at[year, year]

                        if df.at[year, j] < 0:
                            df.at[year, year] = 0
                            profit = False
                        else:
                            df.at[year, year] = df.at[year, j]
                            df.at[year, j] = 0
                            profit = True
                    Sum = self.total_profit_t[year] - df.at[year, year]
                    # '若还有富余，归0
                    if df.at[year, year] > 0:
                        df.at[year, year] = 0
            else:
                # '若当年利润大于0 且后6年时
                if self.total_profit_t[year] > 0:
                    # '取最近5年进行逐年抵扣
                    for j in range(year - 5, year):
                        if j == 2:
                            df.at[year, j] = df.at[year, j] + self.total_profit_t[year]
                        else:
                            df.at[year, j] = df.at[year, j] + df.at[year, year]

                        if df.at[year, j] < 0:
                            df.at[year, year] = 0
                            profit = False
                        else:
                            df.at[year, year] = df.at[year, j]
                            df.at[year, j] = 0
                            profit = True
                    Sum = self.total_profit_t[year] - df.at[year, year]
                    # '若还有富余，归0
                    if df.at[year, year] > 0:
                        df.at[year, year] = 0

            if year == year_final:
                if df.at[year, year] < 0:
                    losses_pre_years = 0
                else:
                    if profit == False:
                        losses_pre_years = self.total_profit_t[year]
                    else:
                        losses_pre_years = Sum

        return losses_pre_years

    def cal_df_03(self):

        self.price_tax_t = [self.eleprice for i in range(0, 22)]
        for year in range(1, 22):

            if year == 1:
                self.ongrid_t[year] = 0
                self.subsidy_income_taxable_t[year] = 0
                self.business_tax_surcharge_t[year] = 0
                self.total_profit_t[year] = 0
                self.taxable_income_t[year] = 0
                self.income_tax_t[year] = 0
                self.subsidy_income_notax_t[year] = 0
                self.net_profit_t[year] = 0
                self.statutory_surplus_reserve_t[year] = 0
                self.price_notax_t[year] = self.price_tax_t[year] / (self.vat / 100 + 1)
            if year > 1:
                self.ongrid_t[year] = self.capacity_mw * self.annual_effective_hours
                self.price_notax_t[year] = self.price_tax_t[year] / (self.vat / 100 + 1)
                self.operating_income_t[year] = self.ongrid_t[year] * self.price_notax_t[year] / 10
                self.vat_t[year] = self.operating_income_t[year] * self.vat / 100
                self.urban_maintenance_tax_sum_t = self.sum_arry(self.urban_maintenance_tax_t[0:year])
                self.education_surcharge_sum_t = self.sum_arry(self.education_surcharge_t[0:year])
                self.vat_sum_t = self.sum_arry(self.vat_t[0:year + 1])
                self.subsidy_income_taxable_sum_t = self.sum_arry(self.subsidy_income_taxable_t[0:year])

                if self.vat_sum_t - self.tax_deduction < 0:
                    self.urban_maintenance_tax_t[year] = 0
                    self.education_surcharge_t[year] = 0
                    self.subsidy_income_taxable_t[year] = 0

                else:
                    self.urban_maintenance_tax_t[year] = (self.vat_sum_t - self.tax_deduction) \
                                                         * self.urban_maintenance_tax / 100 \
                                                         - self.urban_maintenance_tax_sum_t
                    self.education_surcharge_t[year] = (self.vat_sum_t - self.tax_deduction) \
                                                       * self.education_surcharge / 100 \
                                                       - self.education_surcharge_sum_t
                    self.subsidy_income_taxable_t[year] = (self.vat_sum_t - self.tax_deduction) \
                                                          / 2 - self.subsidy_income_taxable_sum_t

                self.business_tax_surcharge_t[year] = self.urban_maintenance_tax_t[year] + \
                                                      self.education_surcharge_t[
                                                          year]
                self.total_profit_t[year] = self.operating_income_t[year] - self.business_tax_surcharge_t[
                    year] - self.total_cost[year] + self.subsidy_income_taxable_t[year]

                self.offset_prior_losses = self.cal_losses_pre_years(year)
                self.offset_prior_losses_t[year] = self.offset_prior_losses

                if self.total_profit_t[year] < 0:
                    self.taxable_income_t[year] = 0
                else:
                    self.taxable_income_t[year] = self.total_profit_t[year] - self.offset_prior_losses_t[year]

                self.income_tax_t[year] = self.taxable_income_t[year] * self.it_rate / 100
                self.subsidy_income_notax_t[year] = 0
                self.net_profit_t[year] = self.total_profit_t[year] - self.income_tax_t[year] + \
                                          self.subsidy_income_notax_t[year]

                # 0
                self.undistributed_profit_f_t[year] = self.net_profit_t[year - 1] + self.undistributed_profit_f_t[
                    year - 1] - self.statutory_surplus_reserve_t[year - 1] - self.profit_payable_t[year - 1]
                # 1
                self.distributed_profit_t[year] = self.net_profit_t[year] + self.undistributed_profit_f_t[year]

                # 1
                if self.net_profit_t[year] < 0:
                    self.statutory_surplus_reserve_t[year] = 0
                else:
                    self.statutory_surplus_reserve_t[year] = self.net_profit_t[year] * self.ssr_rate / 100

                # 2
                self.profits_available_investor_t[year] = self.distributed_profit_t[year] - \
                                                          self.statutory_surplus_reserve_t[year]

                self.surplus_reserve_fund_t[year] = self.net_profit_t[year] * self.dsp_rate / 100

                # 3
                if self.profits_available_investor_t[year] < 0:
                    self.profit_payable_t[year] = 0
                else:
                    if sum(self.资本金_投资计划与资金筹措表) * self.profit_payable_rate / 100 >= self.profits_available_investor_t[
                        year]:
                        self.profit_payable_t[year] = self.profits_available_investor_t[year]
                    else:
                        self.profit_payable_t[year] = sum(self.资本金_投资计划与资金筹措表) * self.profit_payable_rate / 100

                self.undistributed_profit_t[year] = self.profits_available_investor_t[year] - \
                                                    self.surplus_reserve_fund_t[
                                                        year] - self.profit_payable_t[year]

                self.edit[year] = self.total_profit_t[year] + self.利息支出[year]
                self.earnings_before_interest[year] = self.edit[year] + self.折旧费[year]


        self.df_03_f = self.arry_dic(self.result,  self.index_name1_03,self.index_name0_03)
        return self.df_03_f


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

    # print(result_03.iloc[:,13:16])
