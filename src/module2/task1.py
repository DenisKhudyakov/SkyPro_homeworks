from typing import Any
from itertools import chain


def non_empty_truths(obj: Any):
    # return list(filter(lambda x: x, chain(*obj)))
    # Дополнительное решение на случай более глубокой вложенности списков
    empty_list = []
    for i in obj:
        if isinstance(i, list):
            new_list = list(filter(lambda x: x, non_empty_truths(i)))
            empty_list.extend(new_list)
        elif i:
            empty_list.append(i)
    yield empty_list


print(*non_empty_truths([[0, 1, 2], [], [], [[False], True, 42]]))
print(*non_empty_truths([[], [[]]]))
