"""6.	Реализовать два небольших скрипта:
●	итератор, генерирующий целые числа, начиная с указанного;
●	итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle()
модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его
завершения. Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

"""
from itertools import count
from itertools import cycle

# ●	итератор, генерирующий целые числа, начиная с указанного;
start = 2
finish = 10


def generator_1(st, fn):
    k = 1
    iter1 = count(st)
    while k <= fn:
        g3 = next(iter1)
        k += 1
        yield g3


g5 = generator_1(start, finish-1)
print(type(g5))


for v in g5:
    print(v)


# ●	итератор, повторяющий элементы некоторого списка, определённого заранее.
first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55] # Заданный список
stop_count = 3 # Заданное условие: количество элементов из заданного списка для повторения
number_of_repetitions = 4 # Заданное условие: количество повторений списка


def generator_on_list(list_in, count_element, count_1):
    j = 1
    while j <= count_1:
        i = 1
        iterate = cycle(list_in)
        while i <= count_element:
            g2 = next(iterate)
            i += 1
            yield g2
        j += 1


g = generator_on_list(first_list, stop_count, number_of_repetitions)
print(f' type(g) =   {type(g)}')

for el in g:
    print(f' el = {el}')
