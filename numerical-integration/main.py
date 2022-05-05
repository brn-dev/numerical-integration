
from integration_rules.rectangle_rule import rectangle_rule_midpoint
from integration_rules.trapezoid_rule import trapezoid_rule
from numerical_integration import NumericalIntegration

N_SLICES = 1000
FROM = 0
TO = 2

def f(x):
    return x * x

def print_rule_result(rule_name: str, result: float):
    print(f'{rule_name}: {result}')

def main():
    print_rule_result(
        'Rectangle rule',
        NumericalIntegration(rectangle_rule_midpoint).approximate_integration(f, FROM, TO, N_SLICES)
    )

    print_rule_result(
        'Trapezoid rule',
        NumericalIntegration(trapezoid_rule).approximate_integration(f, FROM, TO, N_SLICES)
    )


if __name__ == '__main__':
    main()

