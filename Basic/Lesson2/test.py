list_tuple_position = []
list_tuple_position = [(1, {'Название': 'name1', 'Цена': 'sdh', 'Количество': 'ert', 'Единица измерения': 'etry'}),
                       (2, {'Название': 'name2', 'Цена': 'xcg', 'Количество': 'ytr', 'Единица измерения': 'as'}),
                       (3, {'Название': 'name3', 'Цена': 'xcg', 'Количество': 'ytr', 'Единица измерения': 'as'})]
# print(list_tuple_position[0][1]['Название'], len(list_tuple_position))
# print(list_tuple_position[1][1]['Название'])
# print(list_tuple_position[2][1]['Название'])

# Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
# }
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



