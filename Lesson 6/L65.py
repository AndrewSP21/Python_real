"""
5.	Реализовать класс Stationery (канцелярская принадлежность).

●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
●	в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить
    уникальное сообщение;
●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

"""


class Stationery:
    title: str

    def __init__(self, title=''):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):

    def draw(self):
        print(f'Рисуем ручкой "{self.title}"')


class Pencil(Stationery):

    def draw(self):
        print(f'Рисуем карандашом "{self.title}"')


class Handle(Stationery):

    def draw(self):
        print(f'Рисуем маркером "{self.title}"')


a = Stationery()
a.draw()

b = Pen('Bic')
b.draw()

c = Pencil('KOH-I-NOOR')
c.draw()

d = Handle('Комус')
d.draw()