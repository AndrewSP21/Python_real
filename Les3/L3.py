import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

user_table = pd.read_csv('user_table.csv', header=0, sep=',')
home_page = pd.read_csv('home_page_table.csv', header=0, sep=',')
search_page = pd.read_csv('search_page_table.csv', header=0, sep=',')
payment_page = pd.read_csv('payment_page_table.csv', header=0, sep=',')
payment_confirmation = pd.read_csv('payment_confirmation_table.csv', header=0, sep=',')

home_page = home_page.rename(columns={'page': 'home_page'})
search_page = search_page.rename(columns={'page': 'search_page'})
payment_page = payment_page.rename(columns={'page': 'payment_page'})
payment_confirmation = payment_confirmation.rename(columns={'page': 'payment_confirmation'})

from functools import reduce

data_frames = [user_table, home_page, search_page, payment_page, payment_confirmation]
df = reduce(lambda left, right: pd.merge(left, right, on='user_id', how='left'), data_frames)

df['home_page'] = df['home_page'].apply(lambda x: 1 if x == 'home_page' else 0)
df['search_page'] = df['search_page'].apply(lambda x: 1 if x == 'search_page' else 0)
df['payment_page'] = df['payment_page'].apply(lambda x: 1 if x == 'payment_page' else 0)
df['payment_confirmation'] = df['payment_confirmation'].apply(lambda x: 1 if x == 'payment_confirmation_page' else 0)

# print(df.head())
'''
1. Использовать датасет с текущего урока и построить сегментированную воронку конверсии пользователей интернет-магазина по полу.
'''


dfg = df.groupby('sex')[['home_page', 'search_page', 'payment_page', 'payment_confirmation']].sum().unstack('sex').unstack('sex').reset_index()

from plotly import graph_objects as go

# Настраиваем скрипт библиотеки Plotly нашими параметрам
fig = go.Figure()

# Часть графика для типа устройств Dekstop
fig.add_trace(go.Funnel(
    y = dfg['index'],
    x = dfg['Female'],
    name = 'Female',
    constraintext='outside',
    textposition = 'inside',
    textinfo = 'value+percent previous'
    ))

# Часть графика для типа устройств Mobile
fig.add_trace(go.Funnel(
    y = dfg['index'],
    x = dfg['Male'],
    name = 'Male',
    textposition = 'auto',
    textinfo = 'value+percent previous'
   ))

fig.update_layout(
    title = 'Воронка конверсии по полу',
    title_x=0.5,
    autosize=False,
    width=1200,
    height=600)
fig.
fig.savefig('1.png')
# fig.show()
# print(dfg)


'''
2. Создать 2 новые фичи на основе колонки “date”: месяц и день недели (пример https://stackoverflow.com/a/62624729, 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.weekday.html ).
'''


'''Преобразуем столбец в дату'''
df['date'] = pd.to_datetime(df['date'])
'''Добавляем названия месяцев'''
df['month'] = df['date'].dt.month_name(locale = 'Ru') #month
'''TДобалвяем названия дней недели'''
df['weekday'] = df['date'].dt.day_name(locale = 'Ru') #dt.dayofweek
print(df.head())
'''
3. Определить самый топовый по продажам месяц и день недели с помощью базовых методов агрегации (sum или count).
'''
'''Считем сумму оплат помесячно'''
# top_month = df.groupby('month')[['payment_confirmation']].sum().reset_index()
'''The month as January=1, December=12. Добавялем колонку - номера месяцев'''
df['m'] = df['date'].dt.month
'''The day of the week with Monday=0, Sunday=6. Добавляем колонку  номера дней недели'''
df['w'] = df['date'].dt.dayofweek


'''Считем сумму оплат по дням недели'''
# top_weekday = df.groupby('weekday')[['payment_confirmation']].sum().reset_index()
# print(top_weekday)

def counts1(df, column, start, end):
    a = 0
    b = 0

    for el in range(start, end):
        top_m = df[df[column] == el]
        top_m = top_m[['payment_confirmation']].sum()
        if a < top_m.iloc[0]:
            a = top_m.iloc[0]
            b = el
    return b


m = counts1(df, 'm', 1, 12)
w = counts1(df, 'w', 0, 6)

import calendar

print(f'Месяц топовый по продажам: {calendar.month_name[m]}')
'''Выбираем значение из столбца "weekday" '''
print(f'День недели топовый по продажам: {calendar.day_name[w]}')


'''
4. Выяснить, в какой день недели лучше покупают женщины, а в какой мужчины с помощью одного из методов построения 
сводных таблиц (groupby, pivot_table или crosstab).
'''

best_day = pd.pivot_table(df, index = 'sex', columns = 'weekday' , values = 'payment_confirmation', aggfunc = 'sum', margins=False).unstack('sex').unstack('sex')
best_woman_day = best_day[best_day['Female'] == best_day['Female'].max()].reset_index()
best_man_day = best_day[best_day['Male'] == best_day['Male'].max()].reset_index()
# best_man_day.columns.name = None
best_man_day = best_man_day.iloc[0]["weekday"]
best_woman_day = best_woman_day.iloc[0]["weekday"]
print(best_day)
print('---------------------')
print(f'День недели в который мужчины покупают лучше: {best_man_day}')
print(f'День недели в который женщины покупают лучше: {best_woman_day}')

