"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных. """


class Дата:
    def __init__(self, dmy):
        self.dmy = dmy
        self.d, self.m, self.y = self.turn_to_digit(dmy)
        self.validation(self.d, 31)
        self.validation(self.m, 12)
        self.validation(self.y, 2099)

    @classmethod
    def turn_to_digit(cls, param):
        d, m, y = list(map(int, param.split('-')))
        return d, m, y

    @staticmethod
    def validation(x, test):
        if 1 <= x <= test:
            return x
        else:
            print(f'Данные не соответствуют формату. Число {x} должно быть в дипазоне от 1 до {test}.')


a = Дата('05-01-2022')
b = Дата('53-01-2022')
c = Дата('05-21-2022')
d = Дата('05-12-2122')