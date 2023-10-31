def count_number_in_list(number_list: list, number: int) -> int:
    """
    Функция которая принимает список чисел и число, а также возвращает количество раз, когда число встретилось в списке.
    :param number_list: list
    :param number: int
    :return: int
    """
    return len(list(filter(lambda x: x == number, number_list)))
