from integration_rules.integration_rule import OneDimensionalFunction


def trapezoid(f: OneDimensionalFunction, a: float, b: float) -> float:
    y0 = f(a)
    y1 = f(b)
    h = b - a
    return 0.5 * (y0 + y1) * h
