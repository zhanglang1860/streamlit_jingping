#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ZhangYicheng
@file:main.py
@time:2020/11/24
"""

from results_10 import *
from total_cost_02_b import *
from loan_interest_04b import *
from investment_financing_01 import *
from total_cost_02 import *
from profit_table_03 import *
from loan_interest_04 import *
from financial_plan_cash_flow_05 import *
from funds_statement_08 import *
from balance_sheet_09 import *
import streamlit as st
import numpy as np
import pandas as pd
import base64



def main_cal(filename='result', capacity_mw=50, eleprice=0.29, investment=35000,
             annual_effective_hours=2800):

    ### 计算方式： 1. 1-4 计算第一次的利息支出，
    ###          2.  带入2-3（第一次完毕）；3. 计算4B；4.再带入2-3
    real_01 = InvestmentFinancing(run_time=1, capacity_mw=capacity_mw, eleprice=eleprice, investment=investment,
                                  annual_effective_hours=annual_effective_hours)
    result_01 = real_01.cal_df_01()
    real_02 = TotalCost(result_01, run_time=1, capacity_mw=capacity_mw, eleprice=eleprice, investment=investment,
                        annual_effective_hours=annual_effective_hours)
    result_02 = real_02.cal_df_02()
    real_03 = ProfitTable(result_01, result_02, run_time=1, capacity_mw=capacity_mw, eleprice=eleprice,
                          investment=investment,
                          annual_effective_hours=annual_effective_hours)
    result_03 = real_03.cal_df_03()
    real_04 = LoanInterest(result_01, result_02, result_03, run_time=1, capacity_mw=capacity_mw, eleprice=eleprice,
                           investment=investment, annual_effective_hours=annual_effective_hours)
    result_04 = real_04.cal_df_04()

    #入口
    real_02 = TotalCostB(result_01, result_04, run_time=1, capacity_mw=capacity_mw, eleprice=eleprice, investment=investment,
                         annual_effective_hours=annual_effective_hours)
    result_02 = real_02.cal_df_02()
    real_03 = ProfitTable(result_01, result_02, run_time=1, capacity_mw=capacity_mw, eleprice=eleprice,
                          investment=investment,
                          annual_effective_hours=annual_effective_hours)
    result_03 = real_03.cal_df_03()

    real_04 = LoanInterest(result_01, result_02, result_03, run_time=1, capacity_mw=capacity_mw, eleprice=eleprice,
                           investment=investment, annual_effective_hours=annual_effective_hours)
    result_04 = real_04.cal_df_04()

    real_02 = TotalCostB(result_01, result_04, run_time=1, capacity_mw=capacity_mw, eleprice=eleprice, investment=investment,
                         annual_effective_hours=annual_effective_hours)
    result_02 = real_02.cal_df_02()

    real_03 = ProfitTable(result_01, result_02, run_time=1, capacity_mw=capacity_mw, eleprice=eleprice,
                          investment=investment,
                          annual_effective_hours=annual_effective_hours)
    result_03 = real_03.cal_df_03()
    #第一遍算完


    real_04 = LoanInterestB(result_01, result_02, result_03, run_time=1, capacity_mw=capacity_mw, eleprice=eleprice,
                            investment=investment, annual_effective_hours=annual_effective_hours)
    result_04 = real_04.cal_df_04()


    real_02 = TotalCostB(result_01, result_04, run_time=1, capacity_mw=capacity_mw, eleprice=eleprice, investment=investment,
                         annual_effective_hours=annual_effective_hours)
    result_02 = real_02.cal_df_02()

    real_03 = ProfitTable(result_01, result_02, run_time=1, capacity_mw=capacity_mw, eleprice=eleprice,
                          investment=investment,
                          annual_effective_hours=annual_effective_hours)
    result_03 = real_03.cal_df_03()
    #################

    real_05 = FinancialPlanCashFlow(result_01, result_02, result_03, result_04, run_time=1, capacity_mw=capacity_mw,
                                    eleprice=eleprice,
                                    investment=investment, annual_effective_hours=annual_effective_hours)
    result_05 = real_05.cal_df_05()

    real_06 = InvestmentCF(result_01, result_02, result_03, result_04, result_05, run_time=1, capacity_mw=capacity_mw,
                           eleprice=eleprice,
                           investment=investment, annual_effective_hours=annual_effective_hours)
    result_06 = real_06.cal_df_06()

    real_07 = CapitalCF(result_01, result_02, result_03, result_04, result_05, result_06, run_time=1,
                        capacity_mw=capacity_mw, eleprice=eleprice,
                        investment=investment, annual_effective_hours=annual_effective_hours)
    result_07 = real_07.cal_df_07()

    real_08 = FundsStatement(result_01, result_02, result_03, result_04, result_05, result_06, result_07, run_time=1,
                             capacity_mw=capacity_mw, eleprice=eleprice,
                             investment=investment, annual_effective_hours=annual_effective_hours)
    result_08 = real_08.cal_df_08()

    real_09 = BalanceSheet(result_01, result_02, result_03, result_04, result_05, result_06, result_07, result_08,
                           run_time=1, capacity_mw=capacity_mw, eleprice=eleprice,
                           investment=investment, annual_effective_hours=annual_effective_hours)
    result_09 = real_09.cal_df_09()

    real_10 = Results(result_01, result_02, result_03, result_04, result_05, result_06, result_07, result_08, result_09,
                      run_time=1, capacity_mw=capacity_mw, eleprice=eleprice,
                      investment=investment, annual_effective_hours=annual_effective_hours)
    result_10 = real_10.cal_df_10()

    result = [result_01, result_02, result_03, result_04, result_05, result_06, result_07, result_08, result_09,
              result_10]
    sheet_name_list = ['01投资计划与资金筹措表', '02总成本费用表', '03利润和利润分配表', '04借款还本付息计划表', '05财务计划现金流量表'
        , '06项目投资现金流量表', '07项目资本金现金流量表', '08资金来源与运用表', '09资产负债表', '10财务指标汇总表']

    return result, sheet_name_list

def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders', )
    return winreg.QueryValueEx(key, "Desktop")[0]
# def filedownload(files_list):
#     b64 = base64.b64encode(files_list.encode(data.getBytes("UTF-8"))).decode()  # strings <-> bytes conversions
#     href = f'<a href="data:file/csv;base64,{b64}" download="经济评价.csv">Download CSV File</a>'
#     return href



st.title('风电场经济评价计算')
st.write("")
st.info("调整(风电场容量、电价、投资选项、年有效利用小时数)参数,对风电场进行经济性评估.")
st.write("")
left_column, right_column= st.beta_columns(2)
left_column.markdown('#### 风电场容量')
capacity_mw = left_column.slider('', min_value=0, max_value=500, step=5, value=50)
right_column.markdown('#### 电价')
# eleprice = right_column.slider('', min_value=0.20, max_value=0.650, step=0.001, value=0.29)
eleprice = right_column.text_input('', '0.29')
eleprice=float(eleprice)
st.markdown('#### 年有效利用小时数（小时）')
annual_effective_hours = st.slider('', min_value=1000, max_value=4000, step=1, value=2800)
st.markdown('#### 投资选项')
left_column, right_column= st.beta_columns(2)
investment_radio = left_column.radio('', ('建设投资', '单位千万造价'))
if investment_radio == '建设投资':
    investment = right_column.text_input('建设投资', '35000')
elif investment_radio == '单位千万造价':
    investment = right_column.slider('单位千万造价', min_value=5500, max_value=7000, step=50)

filename='results_经济评价'
res, resname = main_cal(filename='results_经济评价', capacity_mw=capacity_mw, eleprice=eleprice, investment=investment,
                        annual_effective_hours=annual_effective_hours)


cn_10 = ["单位", '数值']
cn = ["合计", '第1年', '第2年', '第3年', '第4年', '第5年', '第6年', '第7年', '第8年', '第9年', '第10年',
      '第11年', '第12年', '第13年', '第14年', '第15年', '第16年', '第17年', '第18年', '第19年',
      '第20年', '第21年']
cn[0] = "合计"

st.table(res[9])

left_column1, left_column2,right_column1, right_column2 = st.beta_columns(4)
detial01 = left_column1.checkbox('详细信息')
if detial01:
    option = st.sidebar.selectbox(
        '你选用的是哪个表?',
        resname[:-1])
    '当数据较多时，可以点击右上角Settings进行宽屏设置'

    res02 = res[resname.index(option)]
    res02 = res02.reset_index()

    if resname.index(option) == 0:
        res02['序号项目'] = res02['序号'] + ' ' + res02['项目']
        res02.loc[(res02.index < 12) & (res02.index > 9), '序号项目'] = res02['项目']
    elif resname.index(option) == 2:
        res02['序号项目'] = res02['序号'] + ' ' + res02['项目']
        res02.loc[res02.index < 3, '序号项目'] = res02['项目']
    else:
        res02['序号项目'] = res02['序号'] + ' ' + res02['项目']
    res02.set_index(['序号项目'], inplace=True)
    res02 = res02.drop(['序号', '项目'], axis=1)

    if resname.index(option) >= 2 and resname.index(option) < 9:
        res02.columns = cn
    if resname.index(option) == 9:
        res02.columns = cn_10
    if resname.index(option) < 2:
        res02['合计'] = res02.sum(axis=1)

    if resname.index(option) < 1:
        res2 = res02.iloc[:, :3].style.format("{:.2f}")
    elif resname.index(option) >= 1 and resname.index(option) < 9:
        res2 = res02.style.format("{:.2f}").set_properties(**{
            # 'background-color': 'grey',
            'font-size': '12pt',
        })
    elif resname.index(option) == 9:
        res2 = res02
    st.table(res2)
    # files_list=res[resname.index(option)].to_csv()
    # st.markdown(filedownload(files_list), unsafe_allow_html=True)

detial02 = left_column2.checkbox('存储')
if detial02:
    expander = st.beta_expander("说明")
    expander.write("已存储在桌面上，文件名为：results_经济评价.xlsx")
    file = os.path.join(get_desktop(), '%s.xlsx') % filename
    writer = pd.ExcelWriter(file + '.xlsx')
    for i in range(0, len(res)):
        res[i].loc[:,'合计'] = res[i].sum(axis=1)
        res[i].to_excel(writer, float_format='%.5f', sheet_name=resname[i])
    writer.save()





# if __name__ == '__main__':
#     import winreg
#     from investment_financing_01 import *
#     from total_cost_02 import *
#     from profit_table_03 import *
#     from loan_interest_04 import *
#     from financial_plan_cash_flow_05 import *
#     from funds_statement_08 import *
#     from balance_sheet_09 import *
#
#     import streamlit as st
#     import numpy as np
#     import pandas as pd
#
#     pd.options.display.float_format = '{:.2f}'.format
#
#     st.title('风电场经济评价计算')
#     st.header('调整参数')
#     st.write("可以调整：风电场容量、电价、投资选项、年有效利用小时数 四个参数 对风电场进行经济性评估")
#     capacity_mw = st.slider('风电场容量', min_value=0, max_value=500, step=5, value=50)
#     eleprice = st.slider('电价', min_value=0.20, max_value=0.65, step=0.01, value=0.29)
#     annual_effective_hours = st.slider('年有效利用小时数（小时）', min_value=1000, max_value=4000, step=1, value=2800)
#
#     investment_radio = st.radio('投资选项', ('建设投资', '单位千万造价'))
#     if investment_radio == '建设投资':
#         investment = st.text_input('建设投资', '35000')
#     elif investment_radio == '单位千万造价':
#         investment = st.slider('单位千万造价', min_value=5500, max_value=7000, step=50)
#
#     filename='results_经济评价'
#     res, resname = main_cal(filename='results_经济评价', capacity_mw=capacity_mw, eleprice=eleprice, investment=investment,
#                             annual_effective_hours=annual_effective_hours)
#
#
#     cn_10 = ["单位", '数值']
#     cn = ["合计", '第1年', '第2年', '第3年', '第4年', '第5年', '第6年', '第7年', '第8年', '第9年', '第10年',
#           '第11年', '第12年', '第13年', '第14年', '第15年', '第16年', '第17年', '第18年', '第19年',
#           '第20年', '第21年']
#     cn[0] = "合计"
#
#     st.table(res[9])
#
#     left_column1, left_column2,right_column1, right_column2 = st.beta_columns(4)
#     detial01 = left_column1.checkbox('详细信息')
#     if detial01:
#         option = st.sidebar.selectbox(
#             '你选用的是哪个表?',
#             resname[:-1])
#         '当数据较多时，可以点击右上角Settings进行宽屏设置'
#
#         res02 = res[resname.index(option)]
#         res02 = res02.reset_index()
#
#         if resname.index(option) == 0:
#             res02['序号项目'] = res02['序号'] + ' ' + res02['项目']
#             res02.loc[(res02.index < 12) & (res02.index > 9), '序号项目'] = res02['项目']
#         elif resname.index(option) == 2:
#             res02['序号项目'] = res02['序号'] + ' ' + res02['项目']
#             res02.loc[res02.index < 3, '序号项目'] = res02['项目']
#         else:
#             res02['序号项目'] = res02['序号'] + ' ' + res02['项目']
#         res02.set_index(['序号项目'], inplace=True)
#         res02 = res02.drop(['序号', '项目'], axis=1)
#
#         if resname.index(option) >= 2 and resname.index(option) < 9:
#             res02.columns = cn
#         if resname.index(option) == 9:
#             res02.columns = cn_10
#         if resname.index(option) < 2:
#             res02['合计'] = res02.sum(axis=1)
#
#         if resname.index(option) < 1:
#             res2 = res02.iloc[:, :3].style.format("{:.2f}")
#         elif resname.index(option) >= 1 and resname.index(option) < 9:
#             res2 = res02.style.format("{:.2f}").set_properties(**{
#                 # 'background-color': 'grey',
#                 'font-size': '12pt',
#             })
#         elif resname.index(option) == 9:
#             res2 = res02
#         st.table(res2)
#
#     detial02 = left_column2.checkbox('存储')
#     if detial02:
#         expander = st.beta_expander("说明")
#         expander.write("已存储在桌面上，文件名为：results_经济评价.xlsx")
#         file = os.path.join(get_desktop(), '%s.xlsx') % filename
#         writer = pd.ExcelWriter(file + '.xlsx')
#         for i in range(0, len(res)):
#             res[i].loc[:,'合计'] = res[i].sum(axis=1)
#             res[i].to_excel(writer, float_format='%.5f', sheet_name=resname[i])
#         writer.save()
#
#
#     # from subprocess import Popen, PIPE, STDOUT
#     # import sys
#     #
#     # def run_cmd(cmd):
#     #     p = Popen(cmd, shell=False, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
#     #     stdout, stderr = p.communicate()
#     #     return p.returncode, stdout.strip()
#     #
#     # code, out = run_cmd('streamlit run main.py /')
#     # if code:
#     #     print('命令执行成功')
#     # else:
#     #     print('命令执行失败')
#
#
#
#     #
#     # map_data = pd.DataFrame(
#     #     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     #     columns=['lat', 'lon'])
#     #
#     # st.map(map_data)
#
#     # left_column, right_column = st.beta_columns(2)
#     # pressed = left_column.button('Press me?')
#     # if pressed:
#     #     right_column.write("Woohoo!")
#     # chosen = right_column.radio('Sorting hat',
#     #                             ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     # right_column.write(f"You are in {chosen} house!")
#     # expander = st.beta_expander("FAQ")
#     # expander.write("Here you could put in some really, really long explanations...")
