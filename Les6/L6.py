'''
Решить кейс: Руководство решает внедрить фичу “С этим товаром покупают” в Интернет-магазине. Вам предлагается
протестировать фичу на одном из товаров. Для тестирования фичи вам исходя из истории покупок в интернет-магазине
нужно определить ТОП-10 наиболее близких товаров к исходному. Используйте датасет с  практики текущего урока.
Создайте матрицу item-customer (по срокам - товары, по столбцам - покупатели) Проведите оценку мер близости товаров,
получив матрицу item_item_sim_matrix со значениями косинусов между векторами товаров. Отберите ТОП-10 похожих товаров
по StockCode. Выведите список ТОП-10 похожих товаров с названиями (Description) на экран. Исходный товар - StockCode:
23166 Description: MEDIUM CERAMIC TOP STORAGE JAR
'''
import numpy as np
# Импортируем нужные библиотеки
import pandas as pd

# df = pd.read_excel('http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx')
# df = pd.read_excel('Online Retail.xlsx')
# # Чистим датасет: удаляем записи с нулевыми покупками
# df = df.loc[df['Quantity'] > 0]
# # Чистим датасет: удаляем записи с пропусками в customer_id
# df = df.dropna(subset=['CustomerID'])
# df.to_excel('OnlineRetail_corr.xlsx', sheet_name='new_sheet_name')

df = pd.read_excel('OnlineRetail_corr.xlsx')
# Агрегируем данные в сводную таблицу "товар - покупатель"
item_customer_matrix = df.pivot_table(index='StockCode', columns='CustomerID', values='Quantity', aggfunc='sum')
# Заменяем кол-во покупок на событие: 1- факт покупки, 0 - отсутствие покупки
item_customer_matrix = item_customer_matrix.applymap(lambda x: 1 if x > 0 else 0)
m = item_customer_matrix.values

# Импортируем библиотеку для создания разреженной матрицы
from scipy.sparse import csr_matrix


# Задаем функцию расчета косинуса между векторами-строками товаров
def cos_sim(array):
    # преобразуем
    csr_array = csr_matrix(array)
    numerator = np.dot(csr_array, csr_array.T).toarray()
    denomenator = np.linalg.norm(array, axis=1, keepdims=True) * np.linalg.norm(array.T, axis=0, keepdims=True)
    return numerator / denomenator


# Вычисляем косинусную меру сходства между векторами-строками товаров
item_item_sim_matrix = cos_sim(m)
# Добавляем название столбцов и индексов в матрицу мер близости между векторами-строками товаров
item_item_sim_matrix = pd.DataFrame(item_item_sim_matrix)
item_item_sim_matrix.columns = item_customer_matrix.index
item_item_sim_matrix['StockCode'] = item_customer_matrix.index
item_item_sim_matrix = item_item_sim_matrix.set_index('StockCode')

# На примере эталонного товара находим ТОП-10 товаров, которые близки к нему по косинусной мере
top10 = item_item_sim_matrix.loc[23166].sort_values(ascending=False).head(11).reset_index()
top10 = top10['StockCode']
result = df.loc[df['StockCode'].isin(set(top10)), ['StockCode', 'Description']].drop_duplicates().set_index('StockCode')
result = result.reset_index()
# print(result)
ddd = result.loc[result['StockCode'] == 23166]
ddd = ddd['Description'].values[0]
print(f'ТОП-10 товаров похожих на "{ddd}":')
print(result.loc[result['StockCode'] != 23166]['Description'].reset_index()['Description'])
#Получилось ТОП-11, а не ТОП-10, потому что StockCode 23306 имеет два значения Description
print(result.loc[result['StockCode'] == 23306])