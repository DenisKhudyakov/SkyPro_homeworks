import pytest

from src.module1.my_slice import my_slice

from typing import Any
@pytest.mark.parametrize('coll, start, end, result', [([1, 2, 3, 4, 5, 6], 0, None, [1, 2, 3, 4, 5, 6]),
                                                      ([1, 2, 3, 4, 5, 6], 1, 3, [2, 3]),
                                                      ([1, 2, 3, 4, 5, 6], 1, 4, [2, 3, 4]),
                                                      ([1, 2, 3, 4, 5, 6], 1, 10, [2, 3, 4, 5, 6]),
                                                      ([1, 2, 3, 4, 5, 6], 1, -2, [2, 3, 4]),
                                                      ([1, 2, 3, 4, 5, 6], 0, -2, [1, 2, 3, 4]),
                                                      ([1, 2, 3, 4, 5, 6], 0, -10, []),
                                                      ([], 0, None, [])])


def test_my_slice(coll: list, start: int, end: Any, result: Any) -> None:
    assert my_slice(coll, start, end) == result