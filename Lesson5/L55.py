"""5.	Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
with open(r"additionally/for_L55.txt", "w", encoding="utf") as obj_f:
    str_1 = "1 12 35 675 2 12 76 89 5 234 12 5 354 2 1 523 2"
    obj_f.write(str_1)


with open(r"additionally/for_L55.txt", "r", encoding="utf") as obj_f1:
    str_2 = obj_f1.read()
    s = sum([float(s) for s in str_2.split() if s.isdigit()])
    print(f'Сумма чисел в фале = {s}')


# line1 = str_1.split()
# print(str_1, type(str_1))
# print(line1, type(line1))


