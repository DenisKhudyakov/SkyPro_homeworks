from itertools import chain
from typing import Any, Callable


def is_have(x):
    return True if x else False


def is_int(x):
    return isinstance(x, int)


def each2d(test: bool, matrix: list) -> bool:
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


def some2d(test: Callable[[Any], Any], matrix: list) -> bool:
    """
    функиця должна проверить, удовлетворяет ли предикату
    test хотя бы один элемент матрицы matrix. Как только test возвращает True
    для какого-либо элемента, функция должна вернуть True, в противном случае
    (если ни один элемент проверку не прошел) нужно вернуть False.
    :param test:
    :param matrix:
    :return:
    """
    return any(map(test, chain(*matrix)))


print(some2d(is_have, [[1, 1], ["", 4]]))
print(some2d(is_have, [["", ""], ["", None]]))


def sum2d(test: Any, matrix: list) -> Any:
    """
    Функция, которая возвращает сумму, всех элементов матрицы
    :param test:
    :param matrix:
    :return:
    """
    return sum(filter(test, chain(*matrix)))


print(some2d(is_int, []))
print(sum2d(is_int, [[1, "Foo", 100], [False, 10, None]]))
