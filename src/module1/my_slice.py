from typing import Any
def my_slice(coll: list, start: int=0, end: Any=None):
    """
    Возвращает новый массив, содержащий копию части исходного массива.
    :param coll: исходный список.
    :param start: индекс, по которому начинается извлечение. Если индекс отрицательный,
    start указывает смещение от конца списка. По умолчанию равен нулю.
    :param end: индекс, по которому заканчивается извлечение (не включая элемент с индексом end).
    Если индекс отрицательный, end указывает смещение от конца списка. По умолчанию равен длине исходного списка.
    :return: массив элементов
    """
    length = len(coll)

    if length == 0:
        return []

    normalized_end = length if end is None else end

    normalized_start = start

    if normalized_start < 0:
        if normalized_start < -length:
            normalized_start = 0
        else:
            normalized_start += length

    return coll[normalized_start:normalized_end]


print(my_slice([1, 2, 3, 4, 5, 6], 1, 3))
print(my_slice([1, 2, 3, 4, 5, 6], 1, 3))
print(my_slice([1, 2, 3, 4, 5, 6], 1, 4))
print(my_slice([1, 2, 3, 4, 5, 6], -10, 6))
