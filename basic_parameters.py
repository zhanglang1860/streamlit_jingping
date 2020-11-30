#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Zhangyicheng
@file:basic_parameters.py
@time:2020/11/05
"""


class BasicParametersDefault:
    def __init__(self):
        # ===========年限和装机容量=============
        self.cal_y = 21  # 计算期（年）
        self.building_y = 1  # 建设期（年）
        self.capacity_mw = 50  # 装机容量（MW）
        self.start_building_y = 2015  # 建设期起始年
        self.start_building_m = 1  # 建设期起始月
        self.first_building_m = 12  # 第一年施工月数
        self.last_building_m = 12  # 最后一年施工月数
        # ===========建设期分年度投资=============
        self.investment = 35000  # 分年度投资（万元）
        self.ia = 0  # 无形资产（万元）
        self.other_assets = 0  # 其他资产（万元）
        self.tax_deduction = 3500  # 可抵扣税金（万元）
        self.type_interest_building = '自动计算利息'  # 建设期利息计算方式
        # ===========资本金投入=============
        self.type_bi = '等比例投入'  # 资本金投入方式
        self.rate = 20  # 比例（%）
        self.br_capital = 8  # 资本金基准收益率（%）
        self.br_industry_before = 8  # 行业基准收益率（所得税前）（%）
        self.br_industry_after = 7  # 行业基准收益率（所得税后）（%）
        self.wacc = 4.6  # 资本成本率（%）
        # ===========流动资金及短期贷款=============
        self.indicator_per_kw = 30  # 单位千瓦指标（元/kW）
        self.own_liquidity_rate = 30  # 自有流动资金比例（%）
        self.liquidity_loan_rate = 5.35  # 流动资金贷款利率（%）
        self.short_loan_rate = 5.35  # 短期贷款利率（%）
        # ===========长期借款利息=============
        self.scheduled_repayment = 15  # 预定还款期（年）
        self.type_debt = '等额还本利息照付'  # 还本付息方式
        self.long_loan_rate = 5.9  # 长期贷款利率（%）


class BasicParameters:
    def __init__(self):
        # ===========年限和装机容量=============
        self.cal_y = 0  # 计算期（年）
        self.building_y = 0  # 建设期（年）
        self.capacity_mw = 0  # 装机容量（MW）
        self.start_building_y = 0  # 建设期起始年
        self.start_building_m = 0  # 建设期起始月
        self.first_building_m = 0  # 第一年施工月数
        self.last_building_m = 0  # 最后一年施工月数
        # ===========建设期分年度投资=============
        self.investment = 0  # 分年度投资（万元）
        self.ia = 0  # 无形资产（万元）
        self.other_assets = 0  # 其他资产（万元）
        self.tax_deduction = 0  # 可抵扣税金（万元）
        self.type_interest_building = ''  # 建设期利息计算方式
        # ===========资本金投入=============
        self.type_bi = ''  # 资本金投入方式
        self.rate = 0  # 比例（%）
        self.br_capital = 0  # 资本金基准收益率（%）
        self.br_industry_before = 0  # 行业基准收益率（所得税前）（%）
        self.br_industry_after = 0  # 行业基准收益率（所得税后）（%）
        self.wacc = 0  # 资本成本率（%）
        # ===========流动资金及短期贷款=============
        self.indicator_per_kw = 0  # 单位千瓦指标（元/kW）
        self.own_liquidity_rate = 0  # 自有流动资金比例（%）
        self.liquidity_loan_rate = 0  # 流动资金贷款利率（%）
        self.short_loan_rate = 0  # 短期贷款利率（%）
        # ===========长期借款利息=============
        self.scheduled_repayment = 0  # 预定还款期（年）
        self.type_debt = ''  # 还本付息方式
        self.long_loan_rate = 0  # 长期贷款利率（%）

    def default(self):
        BasicParametersDefault.__init__(self)


if __name__ == '__main__':
    a = BasicParameters()
    a.default()

    print(a.type_bi)
