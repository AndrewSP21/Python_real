"""
3.	Реализовать базовый класс Worker (работник).

●	определить атрибуты: name, surname, position (должность), income (доход);
●	последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
    например, {"wage": wage, "bonus": bonus};
●	создать класс Position (должность) на базе класса Worker;
●	в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
    дохода с учётом премии (get_total_income);
●	проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
    проверить значения атрибутов, вызвать методы экземпляров.

"""


class Worker:
    name = str
    surname = str
    position = str
    __income = dict

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self.__income = {"Wage": wage, "Bonus": bonus}

    def income(self):
        return sum(self.__income.values())


class Position(Worker):
    def get_full_name(self):
        fn = self.name + ' ' + self.surname
        print(f'Сотрудник: {fn}')

    def get_total_income(self):
        print(f'Доход с премией: {self.income()}')


a = Position('Павел', 'Иванов', 'Директор', 100000, 30000)
a.get_full_name()
a.get_total_income()
