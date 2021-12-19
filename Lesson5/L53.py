"""
3.	Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32

"""
from statistics import mean

with open(r"additionally/for_L53.txt", encoding='utf') as f_obj:
    content = f_obj.readlines()
    list1 = []
    list2 = []
    for el in content:
        list1 = el.split()
        dict1 = {list1[0]: float(list1[1])}
        list2.append(dict1)
    list3 = []
    list4 = []
    for el1 in list2:
        for el3 in el1:
            list3.append(el1[el3])
        if el1[el3] < 20000:
            list4.append(el3)

    print(f'Средний доход сотрудников: {round(mean(list3),2)}, \nСписок сотрудников имеющих доход ниже 20000: {list4}')
