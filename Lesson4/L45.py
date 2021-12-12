"""5.	Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов
списка. Подсказка: использовать функцию reduce().

"""
from functools import reduce

first_list = [el for el in list(range(100, 1001)) if el % 2 == 0]


def multi(var1, var2):
    return var1 * var2


result = reduce(multi, first_list)
print(result)
