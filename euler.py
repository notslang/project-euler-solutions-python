import sys


def get_int_input(): return int(input().strip())


def sum_natural_numbers_below(x):
    """
    Get the sum of all numbers below x.
    Example: sum_natural_numbers_below(3) = (1 + 2 + 3) = 6

    >>> sum_natural_numbers_below(3)
    6
    >>> sum_natural_numbers_below(100)
    5050
    """
    # use integer division by 2 to avoid rounding errors on large numbers
    return (x * (x + 1)) // 2
