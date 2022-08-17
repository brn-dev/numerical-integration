
import numpy as np

from integration_rules.rectangle_rule import rectangle_rule_midpoint
from integration_rules.trapezoid_rule import trapezoid_rule
from integration_rules.barrel_rule import barrel_rule_1_3, barrel_rule_3_8
from numerical_integration import NumericalIntegration


def print_rule_result(rule_name: str, result: float):
    print(f'{rule_name}: {result}')


def main():
    function_str = input('Function with parameter "x": ')
    x_from = int(input('From: '))
    x_to = int(input('To: '))
    n_slices = int(input('# Slices: '))

    def f(x):
        return eval(function_str)

    print_rule_result(
        'Rectangle rule',
        NumericalIntegration(rectangle_rule_midpoint).approximate_integration(f, x_from, x_to, n_slices)
    )

    print_rule_result(
        'Trapezoidal rule',
        NumericalIntegration(trapezoid_rule).approximate_integration(f, x_from, x_to, n_slices)
    )

    print_rule_result(
        "Simpson's rule 1/3",
        NumericalIntegration(barrel_rule_1_3).approximate_integration(f, x_from, x_to, n_slices)
    )

    print_rule_result(
        "Simpson's rule 3/8",
        NumericalIntegration(barrel_rule_3_8).approximate_integration(f, x_from, x_to, n_slices)
    )


if __name__ == '__main__':
    main()
