'''2)	Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на
данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой. '''


class OwnError(Exception):

    @staticmethod
    def zero_err():
        print('Делить на ноль нельзя!')

    @staticmethod
    def val_err():
        print('Не верное значение, вводить можно только целые числа!')

a, b = input("Введите два числа через запятую: ").split(',')

try:
    c = int(a) / int(b)
except ZeroDivisionError:
    OwnError.zero_err()
except ValueError:
    OwnError.val_err()
else:
    print(f'{a} делить на {b} = {c}')
