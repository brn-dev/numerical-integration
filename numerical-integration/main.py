
from integration_rules.trapezoid_rule import trapezoid
from numerical_integration import NumericalIntegration

def f(x):
    return x * x

def main():

    integration_rule = trapezoid

    numerical_integration = NumericalIntegration(integration_rule)

    print(numerical_integration.approximate_integration(f, 0, 2, 1000))


if __name__ == '__main__':
    main()

