#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Zhangyicheng
@file:cost_parameters.py
@time:2020/11/05
"""


class CostParametersDefault:
    def __init__(self):
        # ===========折旧费=============
        self.residual_rate = 0  # 残值率（%）
        self.depreciation_method = '折旧年限'  # 折旧费计算方式
        self.depreciation_y = 18  # 折旧年限（年）
        # ===========维修费=============
        self.type_maintenance_fee = '各年不同'  # 维修费计算方式
        self.rate_maintenance_fee = [0, 0.5, 0.5, 0.5, 1, 1, 1, 1, 1, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 2, 2, 2, 2,
                                     2]  # 维修费率（%）
        # ===========人工工资及福利=============
        self.type_job = 1  # 劳动岗位类别（类）
        self.type_salary = '各年相同'  # 人工工资及福利计算方式
        self.num_person = 15  # 人员数量
        self.avg_salary = 4.24  # 人工年平均工资（万元）
        self.other_funds = 50  # 福利费及其他（%）
        # ===========保险费=============
        self.type_ip = '各年相同'  # 保险费计算方式
        self.ip_base = '固定资产净值'  # 保险费计算基数
        self.ip_rate = 0  # 保险费率（%）
        # ===========材料费=============
        self.type_material_fee = '各年相同'  # 材料费计算方式
        self.material_fee_quota = 25  # 材料费定额
        # ===========摊销费=============
        self.amortization_ia = 3  # 无形资产摊销（年）
        self.amortization_oa = 4  # 其他资产摊销（年）
        # ===========其他费用=============
        self.other_expenses_name = 1  # 其他费用项
        self.type_other_expenses = '各年相同'  # 其他费用计算方式
        self.other_expenses = 48  # 其他费用1


class CostParameters:
    def __init__(self):
        # ===========折旧费=============
        self.residual_rate = 0  # 残值率（%）
        self.depreciation_method = ''  # 折旧费计算方式
        self.depreciation_y = 0  # 折旧年限（年）
        # ===========维修费=============
        self.type_maintenance_fee = ''  # 维修费计算方式
        self.rate_maintenance_fee = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                     0]  # 维修费率（%）
        # ===========人工工资及福利=============
        self.type_job = 0  # 劳动岗位类别（类）
        self.type_salary = ''  # 人工工资及福利计算方式
        self.num_person = 0  # 人员数量
        self.avg_salary = 0  # 人工年平均工资（万元）
        self.other_funds = 0  # 福利费及其他（%）
        # ===========保险费=============
        self.type_ip = ''  # 保险费计算方式
        self.ip_base = ''  # 保险费计算基数
        self.ip_rate = 0  # 保险费率（%）
        # ===========材料费=============
        self.type_material_fee = ''  # 材料费计算方式
        self.material_fee_quota = 0  # 材料费定额
        # ===========摊销费=============
        self.amortization_ia = 0  # 无形资产摊销（年）
        self.amortization_oa = 0  # 其他资产摊销（年）
        # ===========其他费用=============
        self.other_expenses_name = 0  # 其他费用项
        self.type_other_expenses = ''  # 其他费用计算方式
        self.other_expenses = 0  # 其他费用1

    def default(self):
        CostParametersDefault.__init__(self)


if __name__ == '__main__':
    a = CostParameters()
    a.default()
    print(a.type_other_expenses)
