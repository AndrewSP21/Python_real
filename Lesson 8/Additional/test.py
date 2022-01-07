# # class Auto:
# #     @staticmethod
# #     def get_class_info():
# #         print("Детальная информация о классе")
# #
# #
# # Auto.get_class_info()
#
# class Operations:
#     """
#     Description for the class
#     """
#     class_name: str
#     class_attr: int
#
#     @staticmethod
#     def lower_string(content: str):
#         return content.lower()
#
#     @staticmethod
#     def upper_string(content: str):
#         return content.upper()
#
#     @classmethod
#     def normalize(cls, content: str):
#         a = cls.lower_string(content)
#         return cls.upper_string(a)
#
#
# temp_string = "Hello"
#
# print(Operations.lower_string(temp_string))
# print(Operations.normalize(temp_string))
#
# print(Operations.__dict__)
# print(Operations.__annotations__)

#
# class MyClass:
#     @staticmethod
#     def on_sum_1(param_1, param_2):  # Статический метод
#         return param_1 + param_2
#
#     def on_sum_2(self, param_1, param_2):  # Обычный метод класса
#         return param_1 + param_2
#
#     def on_sum_3(self, param_1, param_2):
#         return MyClass.on_sum_1(param_1, param_2)  # Вызов статического метода
#
# print(MyClass.on_sum_1(20, 30))
# mc = MyClass()
# print(mc.on_sum_2(20, 10))
# print(mc.on_sum_1(40, 30))
# print(mc.on_sum_3(50, 50))


# class MyClass:
#     @classmethod
#     def my_method(cls, param):  # Метод класса
#         print(cls, param)
#
#     def __init__(self):
#         pass
#
# # MyClass.my_method(30)  # Вызов метода через название класса
# mc = MyClass()
# # mc.my_method(70)  # Вызов метода класса через экземпляр
#
# print(MyClass.__name__)
# print(MyClass.__module__)
# print(MyClass.__dict__)
# print(MyClass.__bases__)
# print(MyClass.__init__(mc))
#
# class User:
#     def __init__(self, name, login, passwd, email):
#         self.name = name
#         self.login = login
#         self.passwd = passwd
#         self.email = email
#     def on_get_data(self):
#         print(f"имя: {self.name}, логин: {self.login}, "
#             f"пароль: {self.passwd}, email: {self.email}")
#
#
# u = User("Ivan Ivanov", "IvIv", "11111", "iviv@mail.ru")
# u.on_get_data()
# print(f"1: __name__ - {User.__name__}, \n __module__ - {User.__module__}, \n"
#     f"2: __dict__ - {User.__dict__}, \n __bases__ - {User.__bases__}, \n"
#     f"3: __doc__ - {User.__doc__}, \n __class__ - {User.__class__}, \n"
#     f"4: __init__ - {User.__init__}, \n __hash__ - {User.__hash__}")
#

# name = "John"
# print(hash(name))
# name1 = "John"
# print(hash(name1))

# values = [1, 2, 3]
# print(hash(values))
#
# tup = (1, 2, 3)
# tuqwerp = (1, 2, 3)
# print(hash(tup))
# print(hash(tuqwerp))
#     first_name: str

# class TestClass:
#     values: list
#
#     def __init__(self, attr):
#         self.first_name = attr
#         self.values = []
#
#     def __hash__(self):
#         return hash(self.first_name)
#
#
# a = TestClass("John")
# print(hash(a))
# b = TestClass("John")
# b.values = "John"
# print(hash(b))
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __str__(self):
#         return f"Name and surname: {self.name} {self.surname}"
#
#
# class Teacher(Person):
#     def to_teach(self, subj, *pupils):
#         for el in pupils:
#             el.to_take(subj)
#
#
# class Pupil(Person):
#     def __init__(self, name, surname):
#         super().__init__(name, surname)
#         self.knowledges = []
#
#     def to_take(self, subj):
#         self.knowledges.append(subj)
#
#
# class Subject:
#     def __init__(self, *subjects):
#         self.subjects = list(subjects)
#
#     def my_list(self):
#         return self.subjects
#
#
# s = Subject("maths", "physics", "chemistry")
# t = Teacher("Ivan", "Ivanov")
# p_1 = Pupil("Petr", "Petrov")
# p_2 = Pupil("Sergey", "Sergeev")
# p_3 = Pupil("Vladimir", "Vladimirov")
# # print(f"{p_1}; {p_2}; {p_3}")
#
# t.to_teach(s, p_1, p_2, p_3)
# print(p_2.knowledges[0].my_list())
# # print(p_1.knowledges[1].my_list())
#
# try:
#     res = 100/0
# except ZeroDivisionError:
#     print("На ноль делить нельзя")
# else:
#     print(f"Все хорошо. Результат - {res}")
# finally:
#     print("Программа завершена")
#
# class OwnError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# inp_data = input("Введите положительное число: ")
#
# try:
#     inp_data = int(inp_data)
#     if inp_data < 0:
#         raise OwnError("Вы ввели отрицательное число!")
# except ValueError:
#     print("Вы ввели не число")
# except OwnError as err:
#     print(err)
# else:
# #     print(f"Все хорошо. Ваше число: {inp_data}")
#
# import traceback
#
# def incorrect(a, b):
#     return a / b
#
# try:
#     res = incorrect(5, 0)
# except Exception as e:
#     print('Ошибка:\n', traceback.format_exc())
#
import time

import psutil
# print(psutil.users())
# print(time.ctime(psutil.boot_time()))
# a = time.time()
# # time.sleep(1)
# b = psutil.boot_time()
# c = b - a
#
# print(a.tm_year)

#
# result = time.localtime(1575721830)
# print("результат:", result)
# print("\nгод:", result.tm_year)
# print("tm_hour:", result.tm_hour)


import requests
# response = requests.get("https://ya.ru", {"q": "python language"})
# print(response.status_code)
# # print(response.content)
# print(response.text)
# #  Информация о системных вызовах и контекстных переключателях
# print(psutil.cpu_stats())
#
# #  Информация о диске
# print(psutil.disk_usage("F:"))
#
# #  Информация о состоянии памяти
# print(psutil.virtual_memory())
# print(psutil.net_io_counters())
import requests

resp = requests.get('https://github.com/requests')
print(resp)
print(type(resp))

resp = requests.put('https://github.com/requests/put')
print(resp)
resp = requests.delete('https://github.com/requests/delete')
print(resp)
resp = requests.head('https://github.com/requests/get')
print(resp)
resp = requests.options('https://github.com/requests/get')
print(resp)
