import functools
from typing import Callable, Any
def memoized(func: Callable) -> Callable:
    """
    Декоратор для защиты от повторных повторных аргументов функции
    :param func: Функция, которая умножает аргумент на 10
    :return: Декорируемая функция
    """
    dict_number = {}
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> int:
        if args not in list(dict_number.keys()):
            dict_number[*args] = func(*args, **kwargs)
            return dict_number.get(args)
    return wrapper



@memoized
def f(x):
    print('Calculating...')
    return x * 10

f(1)
f(1)
f(42)
f(42)
f(1)