# my_f = open(r"C:\Users\-\PycharmProjects\pythonProject\Python_real\test\my_file.txt", 'r', encoding='utf')
#

# content = my_f.read()
# print(f'Поток: {my_f}') # поток
# print(f'Весь файл:\n{content}') #Весь файл


# content2 = my_f.readline()
# print(f'Первая строчка: {content2}')
# content2 = my_f.readline()
# print(f'Первая строчка: {content2}')
#
# for el in my_f:
#     c = my_f.readline()
#     print(el)

# content3 = my_f.readlines()
# print(f'Все строки:{content3}')

# for n, el in enumerate(my_f):
#     print(n, el)

# while True:
#     content = my_f.read(100)
#     print(content)
#
#     if not content:
#         break
# my_f.close()


# out_f = open("out_file2.txt", "w")
# # out_f.write("String string string")
#
# str_list = ['stroka_1\n', 'stroka_2\n', 'stroka_3\n']
# out_f.writelines(str_list)
#
# out_f.close()

# with open(r"my_file.txt", encoding='utf') as f_obj:
#     for line in f_obj:
#         print(line)
#
# try:
#     f_obj = open("my_file.txt", encoding='utf')
#     for line in f_obj:
#         print(line)
# except IOError:
#     print("Произошла ошибка ввода-вывода!")
# finally:
#     f_obj.close()



# try:
#     with open("my_file.txt", encoding='utf') as f_obj:
#         for line in f_obj:
#             print(line)
# except IOError:
#     print("Произошла ошибка ввода-вывода!")
#
# f_obj = open("my_file.txt", 'a')
# f_obj.write("\nMy string")
# f_obj.close()
#
# f_obj = open("data.bin", "wb")
# my_var = b"if5s"
# f_obj.write(my_var)
# f_obj.close()

# with open("file.dat", "w+") as f_obj:
#     f_obj.write("another string")
#     f_obj.seek(4)
#     content = f_obj.read()
#     print(content)

# f_obj = open("new_f.txt", "w")
# print("Файл. Имя: ", f_obj.name)
# print("Файл. Закрыт: ", f_obj.closed)
# print("Файл. Режим: ", f_obj.mode)
# f_obj.close()
# print("Файл. Закрыт: ", f_obj.closed)

# f_obj = open("new_f.txt", "r")
# content = f_obj.read()
# print(content)
# content = f_obj.read()
# print(content)
# f_obj.close()
#
#
# f_obj = open("new_f.txt")
# f_obj.read(10)
# print("Текущая позиция:", f_obj.tell())
# f_obj.close()

# f_obj = open("new_f.txt")
# print(f_obj.read(4))
# print("Мы находимся на позиции1: ", f_obj.tell())
# # Перемещаемся в начало
# f_obj.seek(5)
# print("Мы находимся на позиции2: ", f_obj.tell())
# print(f_obj.read(10))
# f_obj.close()

#
# with open("python2.txt", "w", encoding='utf') as f_obj:
# #     print("Необычная работа функции print", file=f_obj)
# import os
# # os.rename("pytest2.txt", "pytest3.txt")
# # os.remove("pytest3.txt")
#
# # content = os.listdir(path = ".")
# # print(content)
# # content = os.listdir()
# # print(content)
# # content = os.listdir(path="..")
# # print(content)
#
# print(os.path.basename(r"C:\Users\Администраторs8769lugkyfjd\settings.py"))
#
# print(os.path.dirname(r"C:\Users\Администратор\settings.py"))
# print(os.path.exists(r"C:\Users\Администратор\settings.py"))
# print(os.path.isdir(r"C:\Users\Администратор\settings.py"))
# print(os.path.isfile(r"C:\Users\Администратор\settings.py"))
# print(os.path.join(r"C:\Users\Администратор", "settings.py"))
# (os.path.split(r"C:\Users\Администратор\settings.py"))

import json
# data = {
#     "income": {
#         "salary": 50000,
#         "bonus": 20000
#     }
# }
# with open("my_file2.json", "a") as write_f:
#     json.dump(data, write_f)
#     json_str = json.dumps(data)
#     (json_str)
#     (type(json_str))
#
# with open("my_file_fake.json", "a") as f_obj:
#     f_obj.write(str(data))

# with open("my_file_fake.json", "r") as read_f:
#     data = json.load(read_f)
#
# (data)
# (type(data))
#
# json_str = """{"income": {"salary": 50000, "bonus": 20000}}"""
# data = json.loads(json_str)
#
# print(data)
# print(type(data))
#
# with open("my_file3.json", "a") as write_f:
#     json.dump(data, write_f)

#
# import shutil


#
# # shutil.copy("my_file3.json", r"C:\Users\-\PycharmProjects\pythonProject\Python_real\Lesson5")
# #
# # shutil.copy("my_file3.json", r"my_file4.json")
#
# # shutil.copy(r"C:\Users\-\PycharmProjects\pythonProject\Python_real\test", r"C:\Users\-\PycharmProjects\pythonProject"
# #                                                                           r"\Python_real\Lesson5")
#
# shutil.rmtree(r"C:\Users\-\PycharmProjects\pythonProject\Python_real\test\12")

# import sys
#
# # print(sys.argv)
# # print(sys.executable)
# # sys.exit(3)
# print(sys.path)
# print(sys.platform)

import os
os.remove(r"/Python_real/Basic/Lesson5\my_file3.json")