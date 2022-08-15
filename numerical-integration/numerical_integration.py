from typing import Union

from integration_rules.integration_rule import IntegrationRule, OneDimensionalFunction


# noinspection PyMethodMayBeStatic
class NumericalIntegration:

    __integration_rule: IntegrationRule

    def __init__(self, integration_rule: IntegrationRule):
        if not callable(integration_rule):
            raise ValueError(f'Parameter integration_rule ({integration_rule}) is not a valid integration rule!')
        self.__integration_rule = integration_rule

    def __check_f(self, f: OneDimensionalFunction):
        if not callable(f):
            raise ValueError(f'f ({f}) is not a valid one dimensional function!')

    def __check_interval(self, a: Union[int, float], b: Union[int, float]):
        if not (isinstance(a, float) or isinstance(a, int)):
            raise ValueError(f'a ({a}) is not a float!')
        if not (isinstance(b, float) or isinstance(b, int)):
            raise ValueError(f'b ({b}) is not a float!')

    def __check_n_slices(self, n_slices: int):
        if not isinstance(n_slices, int):
            raise ValueError(f'n_slices ({n_slices}) is not an int!')
        if n_slices < 1:
            raise ValueError(f'n_slices ({n_slices}) has to be bigger than 0!')

    def approximate_integration(
            self,
            f: OneDimensionalFunction,
            a: Union[int, float],
            b: Union[int, float],
            n_slices: int
    ) -> float:
        self.__check_f(f)
        self.__check_interval(a, b)
        self.__check_n_slices(n_slices)

        is_reversed = False
        if a == b:
            return 0
        if a > b:
            is_reversed = True
            tmp = a
            a = b
            b = tmp

        area = 0
        x = a
        interval_length = b - a

        for i in range(1, n_slices + 1):
            b = a + i * interval_length / n_slices
            area += self.__integration_rule(f, x, b)
            x = b

        area = round(area, 6)

        if is_reversed:
            area *= -1

        if str(area) == "-0.0":
            area *= -1

        return area
