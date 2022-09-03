# import pandas as pd
#
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', None)
# pd.set_option('display.expand_frame_repr', False)
#
# dfm = pd.read_csv('marketing_campaign.csv', header=0, sep=',')
# dfs = pd.read_csv('subscribers.csv', header=0, sep=',')
# dfu = pd.read_csv('users.csv', header=0, sep=',')
#
# '''
# 1. Взять датасет из домашнего задания №2. Проверить гипотезу о том, в каком варианте теста (control/personalization)
# больше конверсия (converted) и значимо ли это отличие статистически.
# '''
#
# a = dfm.merge(dfu, left_on=['user_id'], right_on=['user_id'], how='left')
# b = a.merge(dfs, left_on=['user_id'], right_on=['user_id'], how='left')
# print(b.head())
# b['converted'] = b['converted'].apply(lambda x: 1 if x is True else 0)
# c = b[['variant', 'converted']]
# c1 = c.groupby('variant')[['converted']].sum().reset_index()
# c2 = c.groupby('variant')[['converted']].count().reset_index()
# c2 = c2.rename(columns={'converted': 'summary'})
# c3 = pd.merge(c1, c2, on='variant', how='left')
# c3['non_converted'] = c3['summary'] - c3['converted']
# df = c3.drop(['summary'], axis=1)
# df = df.set_index('variant')
# print(df.head())
#
# import scipy.stats as stats
#
# result = stats.chi2_contingency(df, correction=False)
# chisq, pvalue = result[:2]
# print('chisq = {}, pvalue = {}'.format(chisq, pvalue))

# Вывод: Так как значимость А/В теста  1.6688675207808698e-29 менее допустимого уровня значимости 0.05, то нулевую
# гипотезу о равенстве конверсий при показе рекламы control и personalization можно отклонить.
# Т.е. конверсия при показе рекламы personalization выше чем при показе control.

# '''2. Цех может производить стулья и столы. На производство стула идет 5 единиц материала, на производство стола - 20
# единиц (футов красного дерева). Стул требует 10 человеко-часов, стол - 15. Имеется 400 единиц материала и 450
# человеко-часов. Прибыль при производстве стула - 45 долларов США, при производстве стола - 80 долларов США. Сколько
# надо сделать стульев и столов, чтобы получить максимальную прибыль?
# '''
#
# '''
# х0 - стульев
# х1 - столов
#
# 45х0 + 80х1 -> max
# 5х0 + 20х1 <= 400
# 10х0 + 15х1 <= 450
# х0 >= 0
# х1 >= 0
#
# '''
# # Задаем целевую функцию
# # Цех производит столы и стулья
# # х0 - стулья, по $45
# # х1 - столов, по $80
# import numpy as np
#
#
# def value(x):
#     return - 45 * x[0] - 80 * x[1]
#
#
# # Задаем систему ограничений:
# # На производство стула идет 5 единиц материала, на производство стола - 20
# # единиц (футов красного дерева)
# # Материалы:
# # 5х0 + 20х1 <= 400
# #  Стул требует 10 человеко-часов, стол - 15. Имеется 450 человеко-часов.
# # ФОТ рабочего времени:
# # 10х0 + 15х1 <= 450
#
#
# neq_cons = {'type': 'ineq',
#             'fun': lambda x: np.array([400 - 5 * x[0] - 20 * x[1],
#                                        450 - 10 * x[0] - 15 * x[1]])}
# # Формальное ограничение — выпуск продукции должен быть только положительным:
# from scipy.optimize import Bounds
#
# bnds = Bounds([0, 0], [np.inf, np.inf])
#
# # Максимизируем функцию ежемесячной прибыли
# from scipy.optimize import minimize
#
# x0 = np.array([3, 3])
# res = minimize(value, x0, method='SLSQP', constraints=neq_cons, bounds=bnds)
# # print(res.x)
# print(f'Для максимизации прибыли необходимо производить: ')
# print(f'Стульев: {round(res.x[0])}')
# print(f'Столов: {round(res.x[1])}')
# print(f'Тогда прибыль составит {-1 * value([round(res.x[0]), round(res.x[1])])}')

'''3. Средний накопленный доход на пользователя с сайта (cumulative ARPU) составил: day1 0.4$, day3 0.6$, day7 0.8$,
day14 1.10$ , day21 1.30$, day30 1.40$. Подберите аппроксимирующую кривую и сделайте прогноз, сколько в среднем
принесет денег пользователь на 90й день. Обоснуйте выбор одной из аппроксимирующей кривой вида: y = a*b^x или y =
a*ln(x) + b.
day1 0.4$,
day3 0.6$,
day7 0.8$,
day14 1.10$ ,
day21 1.30$,
day30 1.40$
'''
import numpy as np
import pandas as pd

df = pd.DataFrame({'day': [1, 3, 7, 14, 21, 30],
                   'cumulative ARPU': [0.4, 0.6, 0.8, 1.1, 1.3, 1.4]})

# определяем тип возможной кривой по диаграмме рассеяния
import matplotlib.pyplot as plt

plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
plt.scatter(df['day'], df['cumulative ARPU'], label="Original Data")
plt.title('Средний накопленный доход на пользователя с сайта')
plt.xlabel('Дни')
plt.ylabel('ARPU')
# plt.show()
plt.close()


# задаем аппроксимирующую логарифмическую функцию y = a*ln(x) + b
def log_func(x, a, b, c):
    return a * np.log(b + x) + c


# def log_func( x, a, b ):
#     return a * np.log(x) + b


# подбираем оптимальные параметры логарифмияеской функции
from scipy.optimize import curve_fit

log_popt, log_pcov = curve_fit(log_func, df['day'], df['cumulative ARPU'])


# задаем аппроксимирующую функцию y = a*b^x
def exp_func(x, a, b):
    return a * np.power(b, x)


# подбираем оптимальные параметры функции y = a*b^x
exp_popt, exp_pcov = curve_fit(exp_func, df['day'], df['cumulative ARPU'])

# задаем точку прогноза - сколько удержанных пользователей сайта останется на 90й день
projection_endpoint = 90

# задаем значения функции x с помощью метода np.arange и параметры подобранной кривой
log_y_projected = log_func(np.arange(projection_endpoint), *log_popt)
exp_y_projected = exp_func(np.arange(projection_endpoint), *exp_popt)


# смотрим график исходных данных и полученных кривых

plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
plt.scatter(df['day'], df['cumulative ARPU'], label="Original Data")
plt.plot(log_y_projected, label="Log Function Projections")
plt.plot(exp_y_projected, label="Функция: y = a*b^x")
plt.title('Средний накопленный доход на пользователя с сайта')
plt.xlabel('Дни')
plt.ylabel('ARPU')
plt.legend()
# plt.show()

# делаем прогноз удержанных пользователей сайта на 90й день
print('Прогноз кол-ва денег, которые принесет пользователей через 90 дней по log модели', round(log_y_projected[89], 0))
print('Прогноз кол-ва денег, которые принесет пользователей через 90 дней по модели y = a*b^x ', round(exp_y_projected[89], 0))
