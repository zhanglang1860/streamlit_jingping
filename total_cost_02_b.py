# -*- coding: utf-8 -*-

# @Time    : 2020/11/12 8:41

# @Author  : Zhaobin

# @FileName: total_cost_02_b.py

# @Software: PyCharm


from investment_financing_01 import *


class TotalCostB(InvestmentFinancing):

    def __init__(self, df_01,df_04, **kargs):
        InvestmentFinancing.__init__(self, run_time=1, capacity_mw=kargs['capacity_mw'], eleprice=kargs['eleprice'],
                                     investment=kargs['investment'],
                                     annual_effective_hours=kargs['annual_effective_hours'])

        self.df_01_f = df_01
        self.df_01_f['合计'] = 0

        self.df_04_f = df_04
        self.df_04_f['合计'] = 0

        self.columns_name_02 = ['第0年', '第1年', '第2年', '第3年', '第4年', '第5年', '第6年', '第7年', '第8年', '第9年', '第10年',
                                '第11年', '第12年', '第13年', '第14年', '第15年', '第16年', '第17年', '第18年', '第19年',
                                '第20年', '第21年']

        self.index_name0_02 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

        self.index_name1_02 = ['折旧费', '维修费', '工资及福利', '保险费', '材料费', '摊销费', '利息支出', '其他费用', '固定成本', '可变成本', '总成本费用',
                               '经营成本', ]

        self.df_02 = pd.DataFrame(
            np.zeros(len(self.index_name1_02) * len(self.columns_name_02)).reshape(
                (len(self.index_name1_02), len(self.columns_name_02))))
        self.df_02 = self.df_02.T
        self.df_02.columns = self.index_name1_02

        # 计算"折旧费"
        self.depreciation_charge_sum = self.fund_raising_detailed[1] - self.tax_deduction  # 计算全部折旧费
        self.depreciation_charge_per_y = self.depreciation_charge_sum / self.depreciation_y  # 计算每年折旧费
        self.depreciation_charge_per_y_list = [0 for i in range(0, self.cal_y - self.building_y)]
        self.depreciation_charge_per_y_arr = np.array(self.depreciation_charge_per_y_list, dtype=float)  # 换算成数组格式
        for i in range(len(self.depreciation_charge_per_y_arr)):  # 循环计算各年折旧费
            if i < self.depreciation_y:
                self.depreciation_charge_per_y_arr[i] = self.depreciation_charge_per_y
            else:
                self.depreciation_charge_per_y_arr[i] = 0
        self.depreciation_charge_building = 0  # 计算建设期折旧
        self.depreciation_charge_sum_arr = np.array(self.depreciation_charge_sum, dtype=float)
        self.depreciation_charge_building_arr = np.array(self.depreciation_charge_building, dtype=float)
        self.depreciation_charge_sum_arr = 0
        self.depreciation_charge_detailed = np.insert(self.depreciation_charge_per_y_arr, 0,
                                                      [self.depreciation_charge_sum_arr,
                                                       self.depreciation_charge_building_arr])  # 计算折旧费明细

        # 计算"维修费"
        self.maintenance_cost_per_y_cal = self.investment - self.tax_deduction  # 计算每年折旧费基数
        self.rate_maintenance_fee_runtime = self.rate_maintenance_fee[1:]  # 得到运行期的维修费率
        self.maintenance_cost_per_y_rate_arr = np.array(self.rate_maintenance_fee_runtime, dtype=float)
        self.maintenance_cost_per_y_arr = self.maintenance_cost_per_y_rate_arr * self.maintenance_cost_per_y_cal / 100  # 计算每年的维修费
        self.maintenance_cost_building = 0  # 计算建设期维修费
        self.maintenance_cost_sum = np.sum(self.maintenance_cost_per_y_arr) + self.maintenance_cost_building  # 计算维修总额
        self.maintenance_cost_building_arr = np.array(self.maintenance_cost_building, dtype=float)
        self.maintenance_cost_sum_arr = np.array(self.maintenance_cost_sum, dtype=float)
        self.maintenance_cost_sum_arr = 0
        self.maintenance_cost_detailed = np.insert(self.maintenance_cost_per_y_arr, 0,
                                                   [self.maintenance_cost_sum_arr,
                                                    self.maintenance_cost_building_arr])  # 计算维修费明细

        # 计算"工资及福利"
        self.wages_benefits_per_y_cal = self.num_person * self.avg_salary * (1 + self.other_funds / 100)  # 计算每年工资福利基数
        self.wages_benefits_per_y = [self.wages_benefits_per_y_cal for i in
                                     range(0, self.cal_y - self.building_y)]  # 计算每年工资福利费用
        self.wages_benefits_per_y_arr = np.array(self.wages_benefits_per_y, dtype=float)
        self.wages_benefits_building = 0  # 计算建设期费用
        self.wages_benefits_building_arr = np.array(self.wages_benefits_building, dtype=float)
        self.wages_benefits_sum = np.sum(self.wages_benefits_per_y_arr) + self.wages_benefits_building  # 计算总额
        self.wages_benefits_sum_arr = np.array(self.wages_benefits_sum, dtype=float)
        self.wages_benefits_sum_arr = 0
        self.wages_benefits_detailed = np.insert(self.wages_benefits_per_y_arr, 0,
                                                 [self.wages_benefits_sum_arr,
                                                  self.wages_benefits_building_arr])  # 计算工资福利明细

        # 计算"保险费"
        self.insurance_premium_per_y_cal = self.depreciation_charge_sum * self.ip_rate  # 计算保费基数
        self.insurance_premium_per_y = [self.insurance_premium_per_y_cal
                                        for i in range(0, self.cal_y - self.building_y)]  # 计算每年保费
        self.insurance_premium_per_y_arr = np.array(self.insurance_premium_per_y, dtype=float)
        self.insurance_premium_building = 0  # 计算建设期保费
        self.insurance_premium_building_arr = np.array(self.insurance_premium_building, dtype=float)
        self.insurance_premium_sum = np.sum(self.insurance_premium_per_y_arr) \
                                     + self.insurance_premium_building  # 计算保费总额
        self.insurance_premium_sum_arr = np.array(self.insurance_premium_sum, dtype=float)
        self.insurance_premium_sum_arr = 0
        self.insurance_premium_detailed = np.insert(self.insurance_premium_per_y_arr, 0,
                                                    [self.insurance_premium_sum_arr,
                                                     self.insurance_premium_building_arr])  # 计算保费明细

        # 计算"材料费"
        self.material_cost_per_y_cal = self.capacity_mw * self.material_fee_quota / 10  # 计算每年材料费基数
        self.material_cost_per_y = [self.material_cost_per_y_cal
                                    for i in range(0, self.cal_y - self.building_y)]  # 计算每年材料费
        self.material_cost_per_y_arr = np.array(self.material_cost_per_y, dtype=float)
        self.material_cost_building = 0  # 计算建设期材料费
        self.material_cost_building_arr = np.array(self.material_cost_building, dtype=float)
        self.material_cost_sum = np.sum(self.material_cost_per_y_arr) + self.material_cost_building  # 计算材料费总额
        self.material_cost_sum_arr = np.array(self.material_cost_sum, dtype=float)
        self.material_cost_sum_arr = 0
        self.material_cost_detailed = np.insert(self.material_cost_per_y_arr, 0,
                                                [self.material_cost_sum_arr,
                                                 self.material_cost_building_arr])  # 计算材料费明细

        # 计算"摊销费"
        self.amortization_fee_per_y_cal = 0  # 计算基数
        self.amortization_fee_per_y = [self.amortization_fee_per_y_cal
                                       for i in range(0, self.cal_y - self.building_y)]  # 每年费用
        self.amortization_fee_per_y_arr = np.array(self.amortization_fee_per_y, dtype=float)
        self.amortization_fee_building = 0  # 建设期费用
        self.amortization_fee_building_arr = np.array(self.amortization_fee_building, dtype=float)
        self.amortization_fee_sum = np.sum(self.amortization_fee_per_y_arr) + self.amortization_fee_building  # 计算总额
        self.amortization_fee_sum_arr = np.array(self.amortization_fee_sum, dtype=float)
        self.amortization_fee_sum_arr = 0
        self.amortization_fee_detailed = np.insert(self.amortization_fee_per_y_arr, 0,
                                                   [self.amortization_fee_sum_arr,
                                                    self.amortization_fee_building_arr])  # 计算明细

        # 计算"利息支出"

        self.interest_expense_per_y = self.df_04_f.loc[pd.IndexSlice['3.5', '利息支出']][2:]
        self.interest_expense_per_y_arr = np.array(self.interest_expense_per_y, dtype=float)
        self.interest_expense_building = 0
        self.interest_expense_building_arr = np.array(self.interest_expense_building, dtype=float)
        self.interest_expense_sum = np.sum(self.interest_expense_per_y_arr) + self.interest_expense_building
        self.interest_expense_sum_arr = np.array(self.interest_expense_sum, dtype=float)
        self.interest_expense_sum_arr = 0
        self.interest_expense_detailed = np.insert(self.interest_expense_per_y_arr, 0,
                                                   [self.interest_expense_sum_arr,
                                                    self.interest_expense_building_arr])

        # 计算"其他费用"
        self.other_expenses_per_y_cal = self.capacity_mw * self.other_expenses / 10  # 计算其他费用基数
        self.other_expenses_per_y = [self.other_expenses_per_y_cal
                                     for i in range(0, self.cal_y - self.building_y)]  # 计算每年其他费用
        self.other_expenses_per_y_arr = np.array(self.other_expenses_per_y, dtype=float)
        self.other_expenses_building = 0  # 计算建设期其他费用
        self.other_expenses_building_arr = np.array(self.other_expenses_building, dtype=float)
        self.other_expenses_sum = np.sum(self.other_expenses_per_y_arr) + self.other_expenses_building  # 计算其他费用总额
        self.other_expenses_sum_arr = np.array(self.other_expenses_sum, dtype=float)
        self.other_expenses_sum_arr = 0
        self.other_expenses_detailed = np.insert(self.other_expenses_per_y_arr, 0,
                                                 [self.other_expenses_sum_arr,
                                                  self.other_expenses_building_arr])  # 计算其他费用明细

        # 计算"固定成本"
        self.fixed_cost_detailed = self.depreciation_charge_detailed + self.maintenance_cost_detailed \
                                   + self.wages_benefits_detailed + self.insurance_premium_detailed \
                                   + self.amortization_fee_detailed + self.interest_expense_detailed \
                                   + self.other_expenses_detailed

        # 计算"可变成本"
        self.variable_cost_detailed = self.material_cost_detailed

        # 计算"总成本费用"
        self.total_cost_detailed = self.fixed_cost_detailed + self.variable_cost_detailed

        # 计算"经营成本"
        self.operating_cost_detailed = self.maintenance_cost_detailed + self.wages_benefits_detailed \
                                       + self.insurance_premium_detailed + self.material_cost_detailed \
                                       + self.amortization_fee_detailed + self.other_expenses_detailed

        self.result = [self.depreciation_charge_detailed, self.maintenance_cost_detailed,
                       self.wages_benefits_detailed, self.insurance_premium_detailed,
                       self.material_cost_detailed, self.amortization_fee_detailed, self.interest_expense_detailed,
                       self.other_expenses_detailed, self.fixed_cost_detailed, self.variable_cost_detailed,
                       self.total_cost_detailed, self.operating_cost_detailed]

    def cal_df_02(self):

        self.df_02_f = self.arry_dic(self.result, self.index_name1_02, self.index_name0_02)

        # self.df_02_f = self.df_02_f.round(2)
        return self.df_02_f


if __name__ == "__main__":
    # pd.options.display.float_format = '{:.2f}'.format
    real_01 = InvestmentFinancing(run_time=1, capacity_mw=50, eleprice=0.29, investment=55000,
                                  annual_effective_hours=2800)
    result_01 = real_01.cal_df_01()

    real_02 = TotalCost(result_01, run_time=1, capacity_mw=50, eleprice=0.29, investment=55000,
                        annual_effective_hours=2800)
    result_02 = real_02.cal_df_02()

    result_02 = result_02.reset_index()
    # result_02.style.format("{:.2f}")
    print(result_02)
    # writer = pd.ExcelWriter('LoanInterest.xlsx')
    # df.to_excel(writer, float_format='%.5f')
    # writer.save()

    import streamlit as st

    st.write(result_02.iloc[:, 2:].style.format("{:.2f}"))
    #

    #
    # result_02 = a.cal_df_02()
    # print(result_02)
