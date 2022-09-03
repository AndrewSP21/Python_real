import pandas as pd
# # создаем датафрейм с результатами A/B-теста
# df = pd.DataFrame({'impressions': [5127, 5127], 'clicks': [1145, 1250]}, index=['var_A', 'var_B'])
# print(df.head())
# # создаем таблицу сопряженности на основе результатов A/B-теста
# df['no_clicks'] = df['impressions'] - df['clicks']
# df = df.drop(['impressions'], axis = 1)
# print(df.head())
# # определяем значимость аб-теста

df = pd.DataFrame({'clicks': [1145, 1250], 'impressions': [5127, 5127]}, index=['var_A', 'var_B'])
import scipy.stats as stats
result = stats.chi2_contingency(df, correction = False)
chisq, pvalue = result[:2]

print(result)

print(f'chisq = {chisq}, pvalue = {pvalue}')

# df = pd.DataFrame({'Day': [1,2,3,4,5,6,7,8,9,10],
#                    'Conversion_A': [0.15,0.12,0.18,0.19,0.17,0.13,0.14,0.23,0.11,0.15],
#                    'Conversion_B': [0.19,0.20,0.18,0.22,0.19,0.17,0.18,0.20,0.17,0.22]})
#
# import matplotlib.pyplot as plt
# from matplotlib.ticker import PercentFormatter
# import seaborn as sns
# plt.figure(figsize=(5, 7))
# ax = sns.boxplot(data=df[['Conversion_A','Conversion_B']], palette="Set2")
# plt.savefig('withoutpercent.png')
# ax.yaxis.set_major_formatter(PercentFormatter(xmax=1))
# plt.savefig('withpercent.png')
#
# import scipy.stats as stats
# t_stat, p_val= stats.ttest_ind(df['Conversion_B'],df['Conversion_A'])
# print(t_stat , p_val)
#
# import numpy as np
#
#
# def value(x):
#     return - 10 * x[0] - 20 * x[1] - 30 * x[2]
#
#
# neq_cons = {'type': 'ineq',
#             'fun': lambda x: np.array([600 - 10 * x[0] - 20 * x[1] - 30 * x[2],
#                                        300 - 7 * x[0] - 15 * x[1] - 20 * x[2],
#                                        150 - 5 * x[0] - 10 * x[1] - 15 * x[2]])}
#
# from scipy.optimize import Bounds
# bnds = Bounds([0, 0, 0], [np.inf, np.inf, np.inf])
#
# from scipy.optimize import minimize
# x0 = np.array([10, 10, 10])
# res = minimize(value, x0, method='SLSQP', constraints=neq_cons, bounds=bnds)
# print(res.x)
#
# print('джуны:', 8 * 10 + 6 * 20 + 3 * 30, 'чел.*час')
# print('мидлы:', 8 * 7 + 6 * 15 + 3 * 20, 'чел.*час')
# print('сеньор:', 8 * 5 + 6 * 10 + 3 * 15, 'чел.*час')
# print('максимизированная прибыль составит:', -1*value([8, 6, 3]),'тыс.руб./месяц')

import pandas as pd
import numpy as np

# df = pd.DataFrame({'day': [0,1,7,14,21,30],
#                    'retained': [100,55,38,26,21,14]})
# print(df.head(6))
#
# import matplotlib.pyplot as plt
# from matplotlib.pyplot import figure
# plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
# plt.scatter(df['day'], df['retained'], label="Original Data" )
# plt.savefig('curve.png')
#
# def log_func( x, a, b, c ):
#     return -a * np.log2( b + x ) + c
#
# def exp_func( x, a, b, c ):
#     return a * np.exp( -b * x ) + c
#
# # подбираем оптимальные параметры логарифмияеской функции
# from scipy.optimize import curve_fit
# log_popt, log_pcov = curve_fit(log_func, df['day'], df['retained'])
#
# # подбираем оптимальные параметры экспоненциальной функции
# exp_popt, exp_pcov = curve_fit(exp_func, df['day'], df['retained'])
#
# # задаем точку прогноза - сколько удержанных пользователей сайта останется на 90й день
# projection_endpoint = 90
#
# # задаем значения функции x с помощью метода np.arange и параметры подобранной кривой
# log_y_projected = log_func( np.arange( projection_endpoint ), *log_popt )
# exp_y_projected = exp_func( np.arange( projection_endpoint ), *exp_popt )
#
# # смотрим график исходных данных и полученных кривых
# import matplotlib.pyplot as plt
# from matplotlib.pyplot import figure
# plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
# plt.scatter(df['day'], df['retained'], label="Original Data" )
# plt.plot( log_y_projected, label="Log Function Projections" )
# plt.plot( exp_y_projected, label="Exp Function Projections" )
# plt.legend()
# # plt.show()
#
# # делаем прогноз удержанных пользователей сайта на 90й день
# print('Прогноз кол-ва пользователей через 90 дней по log модели', round(log_y_projected[89],0))
# print('Прогноз кол-ва пользователей через 90 дней по exp модели', round(exp_y_projected[89],0))
#
# y_log_pred = [log_y_projected[ i ] for i in list(df['day'])]
# print(y_log_pred)
# # отбираем среди прогнозов значения за 0,1,7,14,21 и 30 дни
# y_exp_pred = [exp_y_projected[ i ] for i in list(df['day'])]
# print(y_exp_pred)
