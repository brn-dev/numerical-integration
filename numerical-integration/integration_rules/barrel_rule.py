
from .integration_rule import OneDimensionalFunction


def barrel_rule_1_3(f: OneDimensionalFunction, a: float, b: float) -> float:
    y0 = f(a)
    y1 = f(b)
    h = (b - a)/2
    return h/3 * (y0 + 4*f((a+b)/2) + y1)


def barrel_rule_3_8(f: OneDimensionalFunction, a: float, b: float) -> float:
    y0 = f(a)
    y1 = f(b)
    h = (b - a)/3
    return 3*h/8 * (y0 + 3*f((2*a+b)/3) + 3*f((a+b*2)/3) + y1)
