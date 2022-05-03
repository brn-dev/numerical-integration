
from integration_rules.rectangle_rule import rectangle_rule_midpoint
from numerical_integration import NumericalIntegration

def f(x):
    return x * x

def main():

    integration_rule = rectangle_rule_midpoint

    numerical_integration = NumericalIntegration(integration_rule)

    print(numerical_integration.approximate_integration(f, 0, 2, 1000))


if __name__ == '__main__':
    main()

