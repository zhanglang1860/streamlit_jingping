# -*- coding: utf-8 -*-

# @Time    : 2020/11/10 16:35

# @Author  : Zhaobin

# @FileName: investment_financing_01.py

# @Software: PyCharm

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..\Parameters")))
from basic_parameters import *
from cost_parameters import *
from income_taxes_parameters import *
import numpy as np
import pandas as pd


class InvestmentFinancing(BasicParameters, CostParameters, IncomeTaxesParameters):

    def __init__(self, **kargs):

        if 'run_time' in kargs.keys() and kargs['run_time'] == 1:
            BasicParameters.default(self)
            CostParameters.default(self)
            IncomeTaxesParameters.default(self)

        if 'capacity_mw' in kargs.keys():
            self.capacity_mw = kargs['capacity_mw']
        if 'eleprice' in kargs.keys():
            self.eleprice = kargs['eleprice']
        if 'investment' in kargs.keys():
            self.investment = float(kargs['investment'])
        if 'annual_effective_hours' in kargs.keys():
            self.annual_effective_hours = kargs['annual_effective_hours']

        # 计算"建设投资资本金"
        self.construction_investment_capital_cal = self.investment * (1 + self.long_loan_rate / 100 / 2) \
                                                   / (1 - self.rate / 100) \
                                                   / (100 / self.rate + 100 * (
                1 + self.long_loan_rate / 100 / 2) / (100 - self.rate))

        # 计算"流动资金"
        self.working_capital_cal = self.capacity_mw * self.indicator_per_kw / 10

        # 计算"流动资金资本金"
        self.working_capital_capital_cal = self.working_capital_cal * self.own_liquidity_rate / 100

        # 计算"长期借款本金"
        self.long_loan_principal_cal = self.investment - self.construction_investment_capital_cal

        # 计算"建设期利息"
        self.construction_period_interest_cal = self.long_loan_principal_cal * self.long_loan_rate / 100 / 2

        # 1.1建设投资明细
        self.construction_investment_detailed = [0 for i in range(0, 22)]
        self.construction_investment_detailed[1] = self.investment
        self.construction_investment_sum = sum(self.construction_investment_detailed)

        # 1.2建设期利息
        self.construction_period_interest_detailed = [0 for i in range(0, 22)]
        self.construction_period_interest_detailed[1] = self.construction_period_interest_cal
        self.construction_period_interest_sum = sum(self.construction_period_interest_detailed)

        # 1.3流动资金
        self.working_capital_detailed = [0 for i in range(0, 22)]
        self.working_capital_detailed[2] = self.working_capital_cal
        self.working_capital_sum = sum(self.working_capital_detailed)

        # 1总投资
        self.total_investment_detailed = [0 for i in range(0, 22)]
        self.total_investment_detailed[1] = self.construction_investment_detailed[1] + \
                                            self.construction_period_interest_detailed[1] + \
                                            self.working_capital_detailed[1]
        self.total_investment_detailed[2] = self.construction_investment_detailed[2] + \
                                            self.construction_period_interest_detailed[2] + \
                                            self.working_capital_detailed[2]
        self.total_investment_sum = sum(self.total_investment_detailed)

        # 2.1.1建设投资资本金
        self.construction_investment_capital_detailed = [0 for i in range(0, 22)]
        self.construction_investment_capital_detailed[1] = self.construction_investment_capital_cal
        self.construction_investment_capital_sum = sum(self.construction_investment_capital_detailed)

        # 2.1.2流动资金资本金
        self.working_capital_capital_detailed = [0 for i in range(0, 22)]
        self.working_capital_capital_detailed[2] = self.working_capital_capital_cal
        self.working_capital_capital_sum = sum(self.working_capital_capital_detailed)

        # 2.1资本金（资金筹措）
        self.capital_fund_detailed = [0 for i in range(0, 22)]
        self.capital_fund_detailed[1] = self.construction_investment_capital_detailed[1] + \
                                        self.working_capital_capital_detailed[1]
        self.capital_fund_detailed[2] = self.construction_investment_capital_detailed[2] + \
                                        self.working_capital_capital_detailed[2]
        self.capital_fund_sum = sum(self.capital_fund_detailed)

        # 2.2.1长期借款
        self.long_term_loan_detailed = [0 for i in range(0, 22)]
        self.long_term_loan_detailed[1] = self.long_loan_principal_cal + self.construction_period_interest_cal
        self.long_term_loan_sum = sum(self.long_term_loan_detailed)

        self.长期借款本金 = [0 for i in range(0, 22)]
        self.长期借款本金[1] = self.investment - self.construction_investment_capital_detailed[1]
        self.长期借款本金_合计 = sum(self.长期借款本金)

        self.建设期利息 = [0 for i in range(0, 22)]
        self.建设期利息[1] = self.长期借款本金[1] * self.long_loan_rate / 100 / 2
        self.建设期利息_合计 = sum(self.建设期利息)

        # 2.2.2流动资金借款
        self.working_capital_loan_detailed = [0 for i in range(0, 22)]
        self.working_capital_loan_detailed[2] = self.working_capital_detailed[2] - \
                                                self.working_capital_capital_detailed[2]
        self.working_capital_loan_sum = sum(self.working_capital_loan_detailed)

        # 2.2借款
        self.total_loan_detailed = [0 for i in range(0, 22)]
        self.total_loan_detailed[1] = self.long_term_loan_detailed[1] + self.working_capital_loan_detailed[1]
        self.total_loan_detailed[2] = self.long_term_loan_detailed[2] + self.working_capital_loan_detailed[2]
        self.total_loan_sum = sum(self.total_loan_detailed)

        # 2资金筹措
        self.fund_raising_detailed = [0 for i in range(0, 22)]
        self.fund_raising_detailed[1] = self.capital_fund_detailed[1] + self.total_loan_detailed[1]
        self.fund_raising_detailed[2] = self.capital_fund_detailed[2] + self.total_loan_detailed[2]
        self.fund_raising_sum = sum(self.fund_raising_detailed)

        self.columns_name_01 = ['第0年', '第1年', '第2年', '第3年', '第4年', '第5年', '第6年', '第7年', '第8年', '第9年', '第10年',
                                '第11年', '第12年', '第13年', '第14年', '第15年', '第16年', '第17年', '第18年', '第19年',
                                '第20年', '第21年']

        self.index_name0_01 = ['1', '1.1', '1.2', '1.3', '2', '2.1', '2.1.1', '2.1.2', '2.2', '2.2.1', '2.2.1.1', '2.2.1.2',
                               '2.2.2', ]

        self.index_name1_01 = ['总投资', '建设投资', '建设期利息0', '流动资金', '资金筹措', '资本金（资金筹措）',
                               '建设投资资本金', '流动资金资本金', '借款', '长期借款', '长期借款本金', '建设期利息1', '流动资金借款', ]

        self.df_01 = pd.DataFrame(
            np.zeros(len(self.index_name1_01) * len(self.columns_name_01)).reshape(
                (len(self.index_name1_01), len(self.columns_name_01))))
        self.df_01 = self.df_01.T
        self.df_01.columns = self.index_name1_01
        self.result = [self.total_investment_detailed, self.construction_investment_detailed,
                       self.construction_period_interest_detailed, self.working_capital_detailed,
                       self.fund_raising_detailed, self.capital_fund_detailed,
                       self.construction_investment_capital_detailed,
                       self.working_capital_capital_detailed, self.total_loan_detailed, self.long_term_loan_detailed,
                       self.长期借款本金, self.建设期利息, self.working_capital_loan_detailed]

    def arry_dic(self, result_list, columns_name,index_name):
        dict_df={}
        for ind in range(0, len(columns_name)):
            dict_df[columns_name[ind]] = result_list[ind]
        self.df=pd.DataFrame(dict_df)
        self.df_f = self.df.T
        self.df_f['项目'] = self.df_f.index
        self.df_f['序号'] = index_name
        self.df_f.set_index(['序号', '项目'], inplace=True)
        self.df_f = self.df_f.iloc[:, 1:]
        self.df_f.insert(0, '合计', self.df_f.sum(axis=1))
        return self.df_f
    def arr_df(self, df, result_list, index_name, columns_name):
        for ind in range(0, len(index_name)):
            df.iloc[:, ind] = result_list[ind]

        self.df_f = df.T
        self.df_f.columns = columns_name
        self.df_f['项目'] = self.df_f.index
        self.df_f['序号'] = index_name
        self.df_f.set_index(['序号', '项目'], inplace=True)
        self.df_f = self.df_f.iloc[:, 1:]
        self.df_f.insert(0, '合计', self.df_f.sum(axis=1))
        return self.df_f

    def cal_df_01(self):

        self.df_01_f = self.arry_dic(self.result, self.index_name1_01, self.index_name0_01)

        return self.df_01_f

    # def total_investment(self):
    #     total_investment_number = "1"
    #     total_investment_name = "总投资"
    #     return total_investment_number, total_investment_name, self.total_investment_sum, \
    #            self.total_investment_detailed[1], self.total_investment_detailed[2]
    #
    # def construction_investment(self, investment=35000):
    #     construction_investment_number = "1.1"
    #     construction_investment_name = "建设投资"
    #     return construction_investment_number, construction_investment_name, self.construction_investment_sum, \
    #            self.construction_investment_detailed[1], self.construction_investment_detailed[2]
    #
    # def construction_period_interest(self):
    #     construction_period_interest_number = "1.2"
    #     construction_period_interest_name = "建设期利息"
    #     return construction_period_interest_number, construction_period_interest_name, self.construction_period_interest_sum, \
    #            self.construction_period_interest_detailed[1], self.construction_period_interest_detailed[2]
    #
    # def working_capital(self):
    #     working_capital_number = "1.3"
    #     working_capital_name = "流动资金"
    #     return working_capital_number, working_capital_name, self.working_capital_sum, \
    #            self.working_capital_detailed[1], self.working_capital_detailed[2]
    #
    # def fund_raising(self):
    #     fund_raising_number = "2"
    #     fund_raising_name = "资金筹措"
    #     return fund_raising_number, fund_raising_name, self.fund_raising_sum, \
    #            self.fund_raising_detailed[1], self.fund_raising_detailed[2]
    #
    # def capital_fund(self):
    #     capital_fund_number = "2.1"
    #     capital_fund_name = "资本金（资金筹措）"
    #     return capital_fund_number, capital_fund_name, self.capital_fund_sum, \
    #            self.capital_fund_detailed[1], self.capital_fund_detailed[2]
    #
    # def construction_investment_capital(self):
    #     construction_investment_capital_number = "2.1.1"
    #     construction_investment_capital_name = "建设投资资本金"
    #     return construction_investment_capital_number, construction_investment_capital_name, self.construction_investment_capital_sum, \
    #            self.construction_investment_capital_detailed[1], self.construction_investment_capital_detailed[2]
    #
    # def working_capital_capital(self):
    #     working_capital_capital_number = "2.1.2"
    #     working_capital_capital_name = "流动资金资本金"
    #     return working_capital_capital_number, working_capital_capital_name, self.working_capital_capital_sum, \
    #            self.working_capital_capital_detailed[1], self.working_capital_capital_detailed[2]
    #
    # def total_loan(self):
    #     total_loan_number = "2.2"
    #     total_loan_name = "借款"
    #     return total_loan_number, total_loan_name, self.total_loan_sum, \
    #            self.total_loan_detailed[1], self.total_loan_detailed[2]
    #
    # def long_term_loan(self):
    #     long_term_loan_number = "2.2.1"
    #     long_term_loan_name = "长期借款"
    #     return long_term_loan_number, long_term_loan_name, self.long_term_loan_sum, \
    #            self.long_term_loan_detailed[1], self.long_term_loan_detailed[2]
    #
    # def working_capital_loan(self):
    #     working_capital_loan_number = "2.2.2"
    #     working_capital_loan_name = "流动资金借款"
    #     return working_capital_loan_number, working_capital_loan_name, self.working_capital_loan_sum, \
    #            self.working_capital_loan_detailed[1], self.working_capital_loan_detailed[2]


if __name__ == "__main__":
    #
    IFprint = InvestmentFinancing(run_time=1, capacity_mw=50, eleprice=0.29, investment=35000,
                                  annual_effective_hours=2800)
    result = IFprint.cal_df_01()
    print(result)
    # print(result.loc[pd.IndexSlice['2.2.1','长期借款'],:])

    # print(IFprint.total_investment())
    # print(IFprint.construction_investment())
    # print(IFprint.construction_period_interest())
    # print(IFprint.working_capital())
    # print(IFprint.fund_raising())
    # print(IFprint.capital_fund())
    # print(IFprint.construction_investment_capital())
    # print(IFprint.working_capital_capital())
    # print(IFprint.total_loan())
    # print(IFprint.long_term_loan())
    # print(IFprint.working_capital_loan())
