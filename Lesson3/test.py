def int_func(string: str):
    return ''.join((string[0].upper(), string[1:])) if string else string


def user_temp(string: str):
    return ' '.join(map(int_func, string.split(' ')))


assert int_func('колбаса') == 'Колбаса', "int_func('колбаса')"
assert int_func('самса') == 'Самса', "int_func('самса')"
assert int_func('') == '', "int_func('')"

assert user_temp('колбаса с сыром') == 'Колбаса С Сыром', "user_temp('колбаса с сыром')"
assert user_temp('самса с ветчиной') == 'Самса С Ветчиной', "user_temp('самса с ветчиной')"
assert user_temp('') == '', "user_temp('')"
