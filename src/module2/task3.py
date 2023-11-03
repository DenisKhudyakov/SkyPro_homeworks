def my_map(f, xs):
    """
    Создаем аналог функции map
    :param f: функция
    :param xs: данные
    :return:
    """
    return (f(i) for i in xs)


def my_filter(f, xs):
    """
    Создаем аналог функции filter
    :param f: фукнция
    :param xs: данные
    :return:
    """
    for i in xs:
        if f(i) is True:
            yield i


def replicate_each(n, xs):
    """
    Функция созданяи дубликатов
    :param n: количество копий
    :param xs: данные
    :return:
    """
    for i in xs:
        for _ in range(n):
            yield i


print(list(my_map(abs, [-1, 2, -3])))
print(list(my_filter(lambda x: x % 2 == 1, range(10))))
print(list(replicate_each(1, [1, "a"])))
print(list(replicate_each(3, [1, "a"])))
print(list(replicate_each(0, [1, "a"])))