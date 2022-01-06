import itertools
from _operator import mul


def transpose(it):
    return itertools.zip_longest(it[0], it[1])


def scalar_product(a, b):
    a1 = []
    a2 = []
    for i in a:
        if type(i) == int or type(i) == float:
            a1.append(i)
        elif type(i) == str:
            if i.isdigit():
                a1.append(float(i))
            else:
                return None
        else:
            return None
    for i in b:
        if type(i) == int or type(i) == float:
            a2.append(i)
        elif type(i) == str:
            if i.isdigit():
                a2.append(float(i))
            else:
                return None
        else:
            return None
    return sum(itertools.starmap(mul, itertools.zip_longest(a1, a2)))


expected = [[1, 2], [-1, 3]]
actual = transpose([[1, -1], [2, 3]])
assert expected == list(map(list, actual))

expected = 1
actual = scalar_product([1, '2'], [-1, 1])
assert expected == actual
actual = scalar_product([1, 'xyz'], [-1, 1])
assert actual is None
