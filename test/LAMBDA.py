# #------ "Короткозамкнутые" условные вызовы в Python -----#
# # Обычные управляющие конструкции
# if <cond1>: func1()
# elif <cond2>: func2()
# else: func3()
#
# # Эквивалентное "накоротко замкнутое" выражение
# (<cond1> and func1()) or (<cond2> and func2()) or (func3())
#
# # Пример "накоротко замкнутого" выражения
# >>> x = 3
# >>> def pr(s): return s
# >>> (x==1 and pr('one')) or (x==2 and pr('two')) or (pr('other'))
# 'other'
# >>> x = 2
# >>> (x==1 and pr('one')) or (x==2 and pr('two')) or (pr('other'))
# 'two'
# # pr = lambda s: s
#
# namenum = lambda x: (x == 1 and "one") or (x == 2 and "two") or "other"
#
# print(namenum(1))
# print(namenum(2))
# print(namenum(13))

print([(x, y) for x in (1, 2, 3, 4) for y in (10, 15, 3, 22) if x * y > 25])
