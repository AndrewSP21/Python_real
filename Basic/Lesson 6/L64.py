"""
4.	Реализуйте базовый класс Car.

●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
●	для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40
(WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.

"""
import random


class Car:
    speed: float
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction: str):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        s = random.randint(10, self.speed * 1.2)
        print(f'{self.color} {self.name} текущая скорость: {s} км/ч')


class TownCar(Car):
    max_speed = 60

    def show_speed(self):
        s = random.randint(10, self.speed * 1.2)
        if s > self.max_speed:
            print(f'{self.color} {self.name} текущая скорость: {s} км/ч')
            print(f'Вы превысили скорость на: {s - self.max_speed} км/ч')
        else:
            print(f'{self.color} {self.name} текущая скорость: {s} км/ч')


class WorkCar(Car):
    max_speed = 40

    def show_speed(self):
        s = random.randint(10, self.speed * 1.2)
        if s > self.max_speed:
            print(f'{self.color} {self.name} текущая скорость: {s} км/ч')
            print(f'Вы превысили скорость на: {s - self.max_speed} км/ч', )
        else:
            print(f'{self.color} {self.name} текущая скорость: {s} км/ч')


a = Car(120, 'Белый', 'Мерседес', False)
a.go()
a.show_speed()

b = TownCar(120, 'Красный', 'Ауди', False)
b.stop()
b.go()
b.show_speed()

c = WorkCar(100, 'Желтая', 'Шкода', False)
c.go()
c.turn('направо')
c.show_speed()
