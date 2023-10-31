import pytest

from src.module1.count_number_in_list import count_number_in_list


@pytest.fixture
def data() -> list:
    return [4, 6, 10, 10, 12, 8, 4, 4, 20, 9, 6, 8, 35, 9, 2, 1, 4, 6]


def test_count_number_in_list(data) -> None:
    assert count_number_in_list(data, 4) == 4


def test_count_number_in_list(data) -> None:
    assert count_number_in_list(data, 10) == 2


def test_count_number_in_list(data) -> None:
    assert count_number_in_list(data, 8) == 2


def test_count_number_in_list(data) -> None:
    assert count_number_in_list(data, None) == 0
