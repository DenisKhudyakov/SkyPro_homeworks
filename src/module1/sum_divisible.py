def sum_divisible_by_3_or_5(lst: list) -> int:
    """
    Функция принимает на вход список чисел и возвращает сумму всех элементов списка, которые делятся на 3 или  5 без остатка.
    """
    result = 0
    for num in lst:
        if num % 3 == 0 or num % 5 == 0:
            result += num
    return result
