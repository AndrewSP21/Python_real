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

class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))
