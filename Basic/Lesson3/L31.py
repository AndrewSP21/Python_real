# 1.	Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div():
    try:
        val_1 = float(input('Введите делимое: \n'))
        val_2 = float(input('Введите делитель: \n'))
    except ValueError:
        return print('Делитель и делимое должны быть числами')
    try:
        result = val_1 / val_2
    except ZeroDivisionError:
        return print('Делить на ноль нельзя')
    return print(f'Результат: {round(result, 2)}')


div()
