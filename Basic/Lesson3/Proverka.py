def division(a: float, b: float) -> float:
    """
    делит а на b
    :param a:
    :param b:
    :return: float or None
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        print('Нельзя делить на ноль')


division2 = lambda a, b: a / b if b else None

assert division(4, 2) == 2, 'division(4, 2) SOME TEXT'
assert division(14, 2) == 7, 'division(14, 2)'
assert division(0, 2) == 0, 'division(0, 2)'
assert division(-22, 4) == -5.5, 'division(-22, 4)'
assert division(1, 0) is None, 'division(1, 0)'
