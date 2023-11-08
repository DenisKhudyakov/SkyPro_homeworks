

import functools
from typing import Callable, Any
def memoizing(number: int) -> Callable:
    def wrapper(func: Callable) -> Callable:
        """
        Декоратор для защиты от повторных повторных аргументов функции
        :param func: Функция, которая умножает аргумент на 10
        :return: Декорируемая функция
        """
        dict_number = {}

        @functools.wraps(func)
        def inner(*args: Any, **kwargs: Any) -> int:
            while True:
                if args not in list(dict_number.keys()):
                    dict_number[*args] = func(*args, **kwargs)
                else:
                    if len(list(dict_number.keys())) > number:
                        elem = list(dict_number.keys()).pop(0)
                        del dict_number[elem]
                    return dict_number.get(args)
        return inner
    return wrapper

@memoizing(3)
def f(x):
    print('Calculating...')
    return x * 10

print(f(1))
print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(1))
print(f(1))