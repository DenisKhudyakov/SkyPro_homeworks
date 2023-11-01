import math
from typing import Any


def calculate_area(shape: str, sides: list) -> Any:
    if shape == "круг" and len(sides) == 1:
        return round(2 * math.pi * sides[0], 2)
    elif shape == "квадрат" and len(sides) == 2:
        return sides[0] ** 2
    elif shape == "прямоугольник" and len(sides) == 2:
        return sides[0] * sides[1]
    elif shape == "треугольник" and len(sides) == 3:
        P = (sides[0] + sides[1] + sides[2]) / 2
        return round(math.sqrt(P * (P - sides[0]) * (P - sides[1]) * (P - sides[2])), 2)
    else:
        return None
