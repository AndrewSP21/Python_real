"""7.	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их
прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением
убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.

"""
import json

with open(r"additionally/for_L57.txt", encoding='utf') as f_obj:
    dict1 = {}
    for str1 in f_obj:
        list1 = str1.split()
        list2 = list(map(lambda x: (x.isdigit() and int(x)) or x, list1))
        dict1[list2[0]] = list2[2] - list2[3]
    positive_profit = [x for x in dict1.values() if x > 0]
    average_profit = sum(positive_profit) / len(positive_profit)
    result = [dict1, {'average_profit': average_profit}]
    print(result)

with open("additionally/for_L57.json", "w", encoding='utf') as write_f:
    write_f.write(json.dumps(result, ensure_ascii=False))


