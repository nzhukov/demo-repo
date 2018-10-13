import math


def foo(x=0, y=0):
    """
        Функция, которая считает сумму корней из x

        x - входной аргумент
        y - начальное значение инкремента

    :param x:
    :param y:
    :return float:
    """
    res = 0  # type: int

    while y <= 100:
        res += math.sqrt(x)
        y += 1

    return res


print(foo(2, 1))
