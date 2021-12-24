# class Auto:
#     # атрибуты класса
#     auto_count = 0
#
#     # методы класса
#     def on_auto_start(self, auto_name, auto_model, auto_year):
#         print("Автомобиль заведен")
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year
#         Auto.auto_count += 1
#
#
# a = Auto()
# b = Auto()
# a.on_auto_start("Lexus", "RX 350L", 2019)
# b.on_auto_start("Ауди", "А5", 2021)
# print(a.auto_name)
# print(b.auto_name)
# print(a.auto_count)
# print(b.auto_count)


# class Auto:
#     # атрибуты класса
#     auto_count = 0
#
#     # методы класса
#     def __init__(self):
#         Auto.auto_count += 1
#         print(Auto.auto_count)
#
#
#
# a_1 = Auto()
# a_2 = Auto()
# a_3 = Auto()


# class Auto:
#
#     def get_class_info(self):
#         print("Детальная информация о классе")
#
#
# a = Auto()
# a.get_class_info()

# class Auto:
#     def on_start(self, info):
#         self.info = info
#         # info = "Автомобиль заведен"
#         # return info
#
#
# a = Auto()
# # a.on_start('YYY')
# print(a.info)


# class Auto:
#    info_1 = "Автомобиль заведён"
#
#    def on_start(self):
#        info_2 = "Автомобиль заведён"
#        return info_2
#
# a = Auto()
# print(a.info_1)



#
# class Auto:
#     def __init__(self):
#         print("Автомобиль заведен")
#         self.auto_name = "Mazda"
#         self._auto_year = 2019
#         self.__auto_model = "CX9"
#
# a = Auto()
# print(a.auto_name)
# print(a._auto_year)
# print(a._Auto__auto_model)
#

# class MyClass:
#     _attr = "значение"
#     def _method(self):
#         print("Это защищенный метод!")
#
# mc = MyClass()
# mc._method()
# print(mc._attr)
#
# class MyClass:
#     __attr = "значение"
#     def __method(self):
#         print("Это приватный метод!")
#
# mc = MyClass()
# mc.__method()
# print(mc.__attr)

# class MyClass:
#     __attr = "значение"
#     def __method(self):
#         print("Это защищённый метод!")
#
# mc = MyClass()
# mc._MyClass__method()
# print(mc._MyClass__attr)

# Класс Transport
# class Transport:
#     def transport_method(self):
#         print("Это родительский метод из класса Transport")
#
#
# # Класс Auto, наследующий Transport
# class Auto(Transport):
#     def auto_method(self):
#         print("Это метод из дочернего класса")
#
#
# a = Auto()
# a.transport_method()
# a.auto_method()
#

# класс Transport
# class Transport:
#     def transport_method(self):
#         print("Родительский метод класса Transport")
#
#
# # класс Auto, наследующий Transport
# class Auto(Transport):
#     def auto_method(self):
#         print("Дочерний метод класса Auto")
#
#
# # класс Bus, наследующий Transport
# class Bus(Transport):
#     def bus_method(self):
#         print("Дочерний метод класса Bus")
#
# a = Auto()
# a.transport_method()
# b = Bus()
# b.transport_method()

# class Shape:
#     def __init__(self, color, param_1, param_2):
#         self.color = color
#         self.param_1 = param_1
#         self.param_2 = param_2
#
#     def square(self):
#         return self.param_1 * self.param_2
#
#
# class Rectangle(Shape):
#     def __init__(self, color, param_1, param_2, rectangle_p):
#         super().__init__(color, param_1, param_2)
#         self.rectangle_p = rectangle_p
#
#     def get_r_p(self):
#         return self.rectangle_p
#
#
# class Triangle(Shape):
#     def __init__(self, color, param_1, param_2, triangle_p):
#         super().__init__(color, param_1, param_2)
#         self.triangle_p = triangle_p
#
#     def get_t_p(self):
#         return self.triangle_p
#
# r = Rectangle("white", 10, 20, True)
# print(r.color)
# print(r.square())
# print(r.get_r_p())
# t = Triangle("red", 30, 40, False)
# print(t.color)
# print(t.square())
# print(t.get_t_p())


# class Player:
#     def player_method(self):
#         print("Родительский метод класса Player")
#
#
# class Navigator:
#     def navigator_method(self):
#         print("Родительский метод класса Navigator")
#
#
# class MobilePhone(Player, Navigator):
#     def mobile_phone_method(self):
#         print("Дочерний метод класса MobilePhone")
#
# m_p = MobilePhone()
# m_p.player_method()
# m_p.navigator_method()

# class Shape:
#     def __init__(self, param_1, param_2):
#         self.param_1 = param_1
#         self.param_2 = param_2
#
#     def get_params(self):
#         return f"Параметры Shape: {self.param_1}, {self.param_2}"
#
# class Material:
#     def __init__(self, param_1, param_2):
#         self.param_1 = param_1
#         self.param_2 = param_2
#
#     def get_params(self):
#         return f"Параметры Material: {self.param_1}, {self.param_2}"
#
#
# class Triangle(Shape, Material):
#     def __init__(self, param_1, param_2):
#         super().__init__(param_1, param_2)
#         pass
#
# t = Triangle(10, 20)
# print(t.get_params())

# # класс Auto
# class Auto:
#     def auto_start(self, param_1, param_2=None):
#         if param_2 is not None:
#             print(param_1 + param_2)
#         else:
#             print(param_1)
# a = Auto()
# a.auto_start(50)
# a = Auto()
# a.auto_start(10, 20)

# класс Transport
class Transport:
    def show_info(self):
        print("Родительский метод класса Transport")


# класс Auto, наследующий Transport
class Auto(Transport):
    def show_info(self):
        print("Родительский метод класса Auto")


# класс Bus, наследующий Transport
class Bus(Transport):
    def show_info(self):
        print("Родительский метод класса Bus")

t = Transport()
t.show_info()

a = Auto()
a.show_info()

b = Bus()
b.show_info()
