from typing import Any

import pytest

from src.module1.calculate_area import calculate_area


@pytest.mark.parametrize(
    "name, side, expected_result",
    [
        ("круг", [5], 31.42),
        ("квадрат", [5, 5], 25),
        ("прямоугольник", [5, 20], 100),
        ("треугольник", [20, 20, 20], 173.21),
        ("", [], None),
    ],
)
def test_calculate_area(name: str, side: list, expected_result: Any) -> None:
    assert calculate_area(name, side) == expected_result
