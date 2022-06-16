
from .integration_rule import OneDimensionalFunction


def barrel_rule(f: OneDimensionalFunction, a: float, b: float) -> float:
    y0 = f(a)
    y1 = f(b)
    h = (b - a)/2
    return h/3 * (y0 + 4*f((a+b)/2) + y1)
