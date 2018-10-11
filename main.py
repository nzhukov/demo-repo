import math


def foo(x=0, y=0):
    res = 0  # type: int

    while y <= 100:
        res += math.sqrt(x)
        y += 1

    return res


print(foo(2, 1))
