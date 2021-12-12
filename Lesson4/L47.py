"""7.	Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове
функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n). Она отвечает за
получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!. Подсказка: факториал
числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

"""

from math import factorial


def fact(n):
    i = 1
    while i <= n:
        f = factorial(i)
        i += 1
        yield f


for el in fact(5):
    print(el)

# Или по другому...
from itertools import islice
from itertools import count
from functools import reduce


def multi(var1, var2):
    return var1 * var2


def factorial_new(s):
    t = []
    for i in islice(count(1), s):
        t.append(i)
    result = reduce(multi, t)
    return result


def fact2(n):
    i1 = 1
    while i1 <= n:
        f1 = factorial_new(i1)
        i1 += 1
        yield f1


for el in fact2(5):
    print(el)

# f = factorial_new(4)