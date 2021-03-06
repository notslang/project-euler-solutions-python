#!/bin/python3
from euler import get_int_input, sum_natural_numbers_below


def sum_of_squares(x):
    """
    Get the sum of all squared numbers below x.
    Example: (1**2 + 2**2 + 3**2)

    >>> sum_of_squares(10)
    385
    """
    # use integer division to avoid rounding errors on large numbers
    return (x * (x + 1) * (2 * x + 1)) // 6


def handle_test_case(n):
    """
    Handle the test case.

    >>> handle_test_case(3)
    22
    >>> handle_test_case(10)
    2640
    """
    return (sum_natural_numbers_below(n) ** 2) - sum_of_squares(n)


if __name__ == '__main__':
    number_of_tests = get_int_input()
    for a0 in range(number_of_tests):
        n = get_int_input()
        res = handle_test_case(n)
        print(res)
