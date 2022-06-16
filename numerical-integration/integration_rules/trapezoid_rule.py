
from .integration_rule import OneDimensionalFunction


def trapezoid_rule(f: OneDimensionalFunction, a: float, b: float) -> float:
    y0 = f(a)
    y1 = f(b)
    h = (b - a)/2
    return h * (y0 + y1)
