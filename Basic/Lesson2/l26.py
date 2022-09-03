# 6.	*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
# с параметрами, то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например,
# название. Тогда значение — список значений-характеристик, например, список названий товаров.
#
# Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
# }
print('Введите информацию о товарах')
stop = 'y'
count = 1
list_tuple_position = []
while stop == 'y':
    name = input('Название: ')
    cost = input('Цена: ')
    quantity = input('Количество: ')
    unit_of_measure = input('Единица измерения: ')
    position = {'Название': name, 'Цена': cost, 'Количество': quantity, 'Единица измерения': unit_of_measure}
    tuple_position = (count, position)
    list_tuple_position.append(tuple_position)
    stop = input('Ещё один товар? y/n: ')
    count += 1

count = 0
list_name = []
cost_name = []
quantity_name = []
unit_of_measure_name = []
while count < len(list_tuple_position):
    list_name.append(list_tuple_position[count][1]['Название'])
    cost_name.append(list_tuple_position[count][1]['Цена'])
    quantity_name.append(list_tuple_position[count][1]['Количество'])
    unit_of_measure_name.append(list_tuple_position[count][1]['Единица измерения'])
    count += 1

list_name = list(set(list_name))  # Удаление дублей в списке
cost_name = list(set(cost_name))  # Удаление дублей в списке
quantity_name = list(set(quantity_name))  # Удаление дублей в списке
unit_of_measure_name = list(set(unit_of_measure_name))  # Удаление дублей в списке

slice_name = {'Название': list_name, 'Цена': cost_name, 'Количество': quantity_name,
              'Единица измерения': unit_of_measure_name}
count = 0
print('Название: ', slice_name['Название'])
print('Цена: ', slice_name['Цена'])
print('Количество: ', slice_name['Количество'])
print('Единица измерения: ', slice_name['Единица измерения'])