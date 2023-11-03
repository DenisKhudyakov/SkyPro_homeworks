from typing import Any, Callable
from itertools import chain


def is_have(x):
    return True if x else False


def each2d(test: bool, matrix: list):
    """
    функция должна проверить, что каждый элемент матрицы
    matrix удовлетворяет функции-предикату
    test, и вернуть False, если хотя бы для одного элемента
    test вернул False. В противном случае функция должна возвращать True
    :param test: функция
    :param matrix: список
    :return:
    """
    return all(map(test, chain(*matrix)))


print(each2d(is_have, [[1, 1], ["", 4]]))


def some2d(test, matrix):
    pass


def sum2d(test, matrix):
    pass
