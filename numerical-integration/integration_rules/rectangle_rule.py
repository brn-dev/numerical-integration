
from .integration_rule import OneDimensionalFunction

def rectangle_rule_start(f: OneDimensionalFunction, a: float, b: float) -> float:
    return (b - a) * f(a)

def rectangle_rule_midpoint(f: OneDimensionalFunction, a: float, b: float) -> float:
    return (b - a) * f((a + b) / 2)

def rectangle_rule_end(f: OneDimensionalFunction, a: float, b: float) -> float:
    return (b - a) * f(b)

