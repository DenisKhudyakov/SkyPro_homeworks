from src.module1.sum_divisible import sum_divisible_by_3_or_5


def test_sum_divisible() -> None:
    assert sum_divisible_by_3_or_5([15, 30, 45, 60]) == sum([15, 30, 45, 60])
    assert sum_divisible_by_3_or_5([15, 30, 45, 60, 99, 100, 10]) == sum(
        [15, 30, 45, 60, 99, 100, 10]
    )
    assert sum_divisible_by_3_or_5([15, 30, 45, 60, 99, 100, 10, 8, 7, 14]) == sum(
        [15, 30, 45, 60, 99, 100, 10]
    )
    assert sum_divisible_by_3_or_5([]) == 0
