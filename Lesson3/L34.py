# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# ** Подсказка:** попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def data_entry():
    global x, y
    try:
        x = abs(int(input('Введите действительное положительное число\n')))
    except ValueError:
        return print('Ошибка ввода')
    try:
        y = -abs(int(input('Введите целое отрицательное число\n')))
    except ValueError:
        return print('Ошибка ввода')
    return x, y


def my_func(x, y):
    """
    Функция возвращает возведение х в степень -y
    :param x: Действительное положительное число
    :param y: Целое отрицательное число
    :return: result - возвращает расчет возведения в степень через **,
             result2 - возвращает расчет возведения в степень через цикл
    """
    global result, result2
    result = 1 / (x ** abs(y))
    count = 1
    temp = x
    while abs(y) > count:
        temp = temp * x
        count += 1
    result2 = 1 / temp
    return result, result2


data_entry()
a, b = my_func(x, y)
print(a, b)
