
from typing import Callable

# Function from R to R
OneDimensionalFunction = Callable[[float], float]

# Function that returns the approximate area below a function in a given slice of the interval
# 1st param: The function that should be integrated over
# 2nd param: The start of the interval
# 3rd param: The end of the interval
# Returns: the approximate area of the slice
IntegrationRule = Callable[[OneDimensionalFunction, float, float], float]
