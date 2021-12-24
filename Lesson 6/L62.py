"""
2.	Реализовать класс Road (дорога).

●	определить атрибуты: length (длина), width (ширина);
●	значения атрибутов должны передаваться при создании экземпляра класса;
●	атрибуты сделать защищёнными;
●	определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
●	использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
    толщиной в 1 см*число см толщины полотна;
●	проверить работу метода.

Например: 20 м*5000 м*25 кг*5 см = 12500 т.

"""


class Road:
    __length = float
    __width = float

    def __init__(self, __length, __width):
        self.length = __length
        self.width = __width

    def asphalt_weight(self, weight, height):
        t = round(self.length * self.width * weight * height / 1000)
        result = f'{self.length} м * {self.width} м * {weight} кг * {height} см = {t} т.'
        return print(result)


w = Road(20, 5000)
w.asphalt_weight(25, 5)
