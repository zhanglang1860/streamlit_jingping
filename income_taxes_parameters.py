#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Zhangyicheng
@file:income_taxes_parameters.py
@time:2020/11/05
"""


class IncomeTaxesParametersDefault:
    def __init__(self):
        # ===========产量=============
        self.annual_effective_hours = 2800  # 年有效利用小时数（小时）
        self.type_grid_power_cal = '自动计算上网电量'  # 上网电量计算方式
        self.power_coefficient = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 发电量系数
        # ===========装机进度=============
        self.installed_jan = 0  # 一月装机（MW）
        self.installed_feb = 0  # 二月装机（MW）
        self.installed_mar = 0  # 三月装机（MW）
        self.installed_apr = 0  # 四月装机（MW）
        self.installed_may = 0  # 五月装机（MW）
        self.installed_june = 0  # 六月装机（MW）
        self.installed_july = 0  # 七月装机（MW）
        self.installed_aug = 0  # 八月装机（MW）
        self.installed_sep = 0  # 九月装机（MW）
        self.installed_oct = 0  # 十月装机（MW）
        self.installed_nov = 0  # 十一月装机（MW）
        self.installed_dec = 50  # 十二月装机（MW）
        self.type_gcpg = '本月装机次月并网'  # 并网发电方式
        # ===========电价=============
        self.type_eleprice_cal = '输入电价'  # 电价计算方式
        self.two_stage_eleprice = '否'  # 是否两阶段电价
        self.type_eleprice_input = '电价各年相同'  # 电价输入方式
        self.eleprice = 0.29  # 电价（含增值税）（元/kWh）
        # ===========税率=============
        self.vat = 13  # 增值税税率（%）
        self.type_it_rate = '各年相同'  # 企业所得税税率输入方式
        self.it_rate = 25  # 企业所得税税率（%）
        self.urban_maintenance_tax = 5  # 城市维护建设税（%）
        self.education_surcharge = 3  # 教育费附加（%）
        self.profit_payable_rate = 8  # 应付利润比例（%）
        self.ssr_rate = 10  # 法定盈余公积金比例（%）
        self.dsp_rate = 0  # 任意盈余公积金比例（%）
        self.va_tax_refund50 = True  # 增值税即征即退50%
        self.tax_N_N50 = True  # 所得税N免N减半
        self.free = 3  # 免
        self.halved = 3  # 减半
        # ===========盈利能力分析指标计算采用所得税类型=============
        self.irr_investment = '调整所得税'  # 项目投资财务内部收益率（税后）
        self.npv_investment = '调整所得税'  # 项目投资财务净现值（税后）
        self.payback_period = '调整所得税'  # 项目投资回收期（税后）
        # ===========电价补贴（应税）=============
        self.eps01_name = 1  # 电价补贴项
        self.type_eps01 = '各年相同'  # 电价补贴（元/kWh）
        self.eps01 = 0  # 电价补贴1
        # ===========电价补贴（免税）=============
        self.eps02_name = 1  # 电价补贴项
        self.type_eps02 = '各年相同'  # 电价补贴（元/kWh）
        self.eps02 = 0  # 电价补贴1
        # ===========其他=============
        self.cdm = 0  # CDM项目
        self.subsidy_income_taxable = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 补贴收入（应税）（万元）
        self.subsidy_income_freetax = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 补贴收入（免税）（万元）
        self.benefits_carbon_emissions = False  # 是否考虑碳排放收益


class IncomeTaxesParameters:
    def __init__(self):
        # ===========产量=============
        self.annual_effective_hours = 0  # 年有效利用小时数（小时）
        self.type_grid_power_cal = ''  # 上网电量计算方式
        self.power_coefficient = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 发电量系数
        # ===========装机进度=============
        self.installed_jan = 0  # 一月装机（MW）
        self.installed_feb = 0  # 二月装机（MW）
        self.installed_mar = 0  # 三月装机（MW）
        self.installed_apr = 0  # 四月装机（MW）
        self.installed_may = 0  # 五月装机（MW）
        self.installed_june = 0  # 六月装机（MW）
        self.installed_july = 0  # 七月装机（MW）
        self.installed_aug = 0  # 八月装机（MW）
        self.installed_sep = 0  # 九月装机（MW）
        self.installed_oct = 0  # 十月装机（MW）
        self.installed_nov = 0  # 十一月装机（MW）
        self.installed_dec = 0  # 十二月装机（MW）
        self.type_gcpg = ''  # 并网发电方式
        # ===========电价=============
        self.type_eleprice_cal = ''  # 电价计算方式
        self.two_stage_eleprice = ''  # 是否两阶段电价
        self.type_eleprice_input = ''  # 电价输入方式
        self.eleprice = 0  # 电价（含增值税）（元/kWh）
        # ===========税率=============
        self.vat = 0  # 增值税税率（%）
        self.type_it_rate = ''  # 企业所得税税率输入方式
        self.it_rate = 0  # 企业所得税税率（%）
        self.urban_maintenance_tax = 0  # 城市维护建设税（%）
        self.education_surcharge = 0  # 教育费附加（%）
        self.profit_payable_rate = 0  # 应付利润比例（%）
        self.ssr_rate = 0  # 法定盈余公积金比例（%）
        self.dsp_rate = 0  # 任意盈余公积金比例（%）
        self.va_tax_refund50 = True  # 增值税即征即退50%
        self.tax_N_N50 = True  # 所得税N免N减半
        self.free = 0  # 免
        self.halved = 0  # 减半
        # ===========盈利能力分析指标计算采用所得税类型=============
        self.irr_investment = ''  # 项目投资财务内部收益率（税后）
        self.npv_investment = ''  # 项目投资财务净现值（税后）
        self.payback_period = ''  # 项目投资回收期（税后）
        # ===========电价补贴（应税）=============
        self.eps01_name = 0  # 电价补贴项
        self.type_eps01 = ''  # 电价补贴（元/kWh）
        self.eps01 = 0  # 电价补贴1
        # ===========电价补贴（免税）=============
        self.eps02_name = 0  # 电价补贴项
        self.type_eps02 = ''  # 电价补贴（元/kWh）
        self.eps02 = 0  # 电价补贴1
        # ===========其他=============
        self.cdm = 0  # CDM项目
        self.subsidy_income_taxable = 0  # 补贴收入（应税）（万元）
        self.subsidy_income_freetax = 0  # 补贴收入（免税）（万元）
        self.benefits_carbon_emissions = False  # 是否考虑碳排放收益

    def default(self):
        IncomeTaxesParametersDefault.__init__(self)


if __name__ == '__main__':
    a = IncomeTaxesParameters()
    a.default()
    print(a.type_grid_power_cal)
