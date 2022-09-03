# class MyClass:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def __add__(self, other):
#         return MyClass(self.width + other.width, self.height + other.height)
#
#     def __str__(self):
#         return f"Объект с параметрами ({self.width}, {self.height})"
#
#
# mc_1 = MyClass(10, 20)
# mc_2 = MyClass(30, 40)
# mc_3 = mc_1 + mc_2
# print(mc_3, mc_1, mc_2)

# class MyClass:
#     def __setattr__(self, attr, value):
#         if attr == "width":
#             self.__dict__[attr] = value
#         else:
#             print(f"Атрибут {attr} недопустим")
#
#
# mc = MyClass()
# mc.width = 40
# print(mc.width)

# class Class1:
#     def __init__(self, param):
#         self.param = param
#
#     def __str__(self):
#         return str(self.param)
#
#
# class Class2:
#     def __init__(self, *args):
#         self.my_list = []
#         for el in args:
#             self.my_list.append(Class1(el))
#
#
# my_obj = Class2(10, True, "text")
# print(my_obj.my_list[1])


# class Class1:
#     def __init__(self, param):
#         self.param = param
#
#     def __str__(self):
#        return str(self.param)
#
#
# class Class2:
#     def __init__(self, *args):
#         self.my_list = []
#         for el in args:
#             self.my_list.append(Class1(el))
#
#     def __getitem__(self, index):
#         return self.my_list[index]
#
#
# my_obj = Class2(10, True, "text")
# print(my_obj.my_list[0])
# print(my_obj[1])
# print(my_obj[2])
# class MyClass:
#     def __init__(self, param):
#         self.param = param
#
#     def __call__(self, newparam):
#         self.param = newparam
#
#     def __str__(self):
#         return f"Значение параметра - {self.param};"
#
#
# obj_1 = MyClass("width")
# obj_2 = MyClass("height")
#
# obj_1("length")
# obj_2("square")
#
# print(obj_1, obj_2)
# class MyClass:
#     def __init__(self):
#         self.x = 40
#
#     def __eq__(self, y):
#         return self.x == y
#
#
# mc = MyClass()
# print("Равно" if mc == 40 else "Не равно")
# print("Равно" if mc == 41 else "Не равно")
# class Salary:
#     val = 50000
#
#     def __lt__(self, other):
#         print("Оклад меньше премии?")
#         return self.val < other.val
#
#
# class Prize:
#     val = 5000
#
#     def __lt__(self, other):
#         print("Премия меньше оклада?")
#         return self.val < other.val
#
#
# s = Salary()
# p = Prize()
#
# check = (s < p)
# print(check)
#

# class MyClass:
#     def __init__(self, val):
#         self.val = val
#
#     def __iadd__(self, other):
#         self.val += other
#         return self
#
#
# mc = MyClass(100)
# print(mc.val)
# mc += 200
# print(mc.val)
#
# class ParentClass:
#     def __init__(self):
#         print("Конструктор класса-родителя")
#
#     def my_method(self):
#         print("Метод my_method() класса ParentClass")
#
#
# class ChildClass(ParentClass):
#     def __init__(self):
#         print("Конструктор дочернего класса")
#         ParentClass.__init__(self)
#
#     def my_method(self):
#         print("Метод my_method() класса ChildClass")
#         ParentClass.my_method(self)
#
#
# c = ChildClass()
# c.my_method()

# class ParentClass:
#     def __init__(self):
#         print("Конструктор класса-родителя")
#
#     def my_method(self):
#         print("Метод my_method() класса ParentClass")
#
#
# class ChildClass(ParentClass):
#     def __init__(self):
#         print("Конструктор дочернего класса")
#         super().__init__()
#
#     def my_method(self):
#         print("Метод my_method() класса ChildClass")
#         super().my_method()
#
#
# c = ChildClass()
# c.my_method()

# from abc import ABC, abstractmethod
#
#
# class MyAbstractClass(ABC):
#     @abstractmethod
#     def my_method_1(self):
#         print("Метод my_method_1 из MyAbstractClass()")
#
#     @abstractmethod
#     def my_method_2(self):
#         pass
#
#
# class MyClass(MyAbstractClass):
#     def my_method_1(self):
#         print("Метод my_method_1()")
#
#     def my_method_2(self):
#         print("Метод my_method_2()")
#
#
# mc = MyClass()
# mc.my_method_1()
#
# class Iterator:
#     """
#     Объект-итератор
#     """
#     def __init__(self, start=0):
#         self.i = start
#     # У итератора есть метод __next__
#     def __next__(self):
#         self.i += 1
#         if self.i <= 5:
#             return self.i
#         else:
#             raise StopIteration
#
# class IterObj:
#     """
#     Объект, поддерживающий интерфейс итерации (итерируемый объект)
#     """
#     def __init__(self, start=0):
#         self.start = start - 1
#
#     def __iter__(self):
#         # Метод __iter__ должен возвращать объект-итератор
#         return Iterator(self.start)
#
#
# obj = IterObj(3)
# for el in obj:
#     print(el)
#
# print("Еще раз ...")
# for el in obj:
#     print(el)

#
# class Iter:
#     def __init__(self, start=0):
#         self.i = start - 1
#
#     # Метод __iter__ должен возвращать объект-итератор
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i <= 5:
#             return self.i
#         else:
#             raise StopIteration
#
#
# obj = Iter(2)
# for el in obj:
#     print(el)

# print("Еще раз ...")
# for el in obj:
#     print(el)

# class MyClass:
#     def __init__(self, param_1, param_2):
#         self.param_1 = param_1
#         self.param_2 = param_2
#
#     @property
#     def my_method(self):
#         return f"Параметры, переданные в класс:" \
#             f" {self.param_1}, {self.param_2}"
#
# mc = MyClass("text_1", "text_2")
#
# print(mc.param_1)
# print(mc.param_2)
#
# print(mc.my_method)

# класс Auto
# class Auto:
#
#     # конструктор класса Auto
#     def __init__(self, year):
#         # Инициализация свойств.
#         self.year = year
#
#     # создаем свойство года
#     @property
#     def year(self):
#         return self.__year
#
#     # сеттер для создания свойств
#     @year.setter
#     def year(self, year):
#         if year < 2000:
#             self.__year = 2000
#         elif year > 2019:
#             self.__year = 2019
#         else:
#             self.__year = year
#
#     def get_auto_year(self):
#         return f"Автомобиль выпущен в {str(self.year)} году"
#
# a = Auto(20110)
# print(a.get_auto_year())
#
a = []
print(type(sum(a)))
class WindowDoor:
    def __init__(self, wd_len, wd_height):
        self.square = wd_len * wd_height

class Room:
    def __init__(self, len_1, len_2, height):
        self.square = 2 * height * (len_1 + len_2)
        self.wd = []
    def add_win_door(self, wd_len, wd_height):
        self.wd.append(WindowDoor(wd_len, wd_height))
    def common_square(self):
        main_square = self.square
        for el in self.wd:
            main_square -= el.square
        return main_square


r = Room(7, 4, 3.7)
print(r.square)
r.add_win_door(2, 2)
r.add_win_door(2, 2)
r.add_win_door(2, 2)
print(r.common_square())

