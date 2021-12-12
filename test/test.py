from itertools import islice
from itertools import count
from functools import reduce


def multi(var1, var2):
    return var1 * var2


def factorial_new(s):
    t = []
    for i in islice(count(1), s):
        t.append(i)
    result = reduce(multi, t)
    return result


f = factorial_new(4)
print(f)

