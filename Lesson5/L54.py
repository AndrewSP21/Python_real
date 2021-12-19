"""
4.	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

"""

with open(r"additionally/for_L54.txt", encoding='utf') as f_obj:
    content = f_obj.read()
    content = content.replace('One', 'Один')
    content = content.replace('Two', 'Два')
    content = content.replace('Three', 'Три')
    content = content.replace('Four', 'Четыре')
    with open(r"additionally/for_L54_1.txt", "w", encoding='utf') as f_obj1:
        f_obj1.write(content)

