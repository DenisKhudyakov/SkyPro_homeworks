import pytest

from src.module1.sum_divisible import sum_divisible_by_3_or_5


@pytest.mark.parametrize('data, result', [([15, 30, 45, 60], [15, 30, 45, 60]),
                                          ([15, 30, 45, 60, 99, 100, 10], [15, 30, 45, 60, 99, 100, 10]),
                                          ([15, 30, 45, 60, 99, 100, 10, 8, 7, 14], [15, 30, 45, 60, 99, 100, 10]),
                                          ([], [0])])
def test_sum_divisible(data: list, result: list) -> None:
    assert sum_divisible_by_3_or_5(data) == sum(result)

