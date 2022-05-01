#!/bin/python3

import sys


def get_int_input(): return int(input().strip())


def unit_sum(x):
    """
    Get the sum of all numbers below x.

    >>> unit_sum(3)
    6

    >>> unit_sum(100)
    5050
    """
    # use integer division by 2 to avoid rounding errors on large numbers
    return int((x * (x + 1)) // 2)


def sum_of_multiples_below(max_result, multiplier):
    """
    Get the sum of all multiples of `multiplier` that are below `max_result`.

    >>> sum_of_multiples_below(10, 3)
    18

    >>> sum_of_multiples_below(10, 5)
    5
    """
    # this is the same as sum(range(0, max_result, multiplier)), but faster
    return unit_sum((max_result - 1) // multiplier) * multiplier


def handle_test_case(n):
    """
    Handle the test case.

    >>> handle_test_case(10)
    23
    >>> handle_test_case(100)
    2318
    """
    multiples_of_3 = sum_of_multiples_below(n, 3)
    multiples_of_5 = sum_of_multiples_below(n, 5)
    multiples_of_15 = sum_of_multiples_below(n, 15)

    return multiples_of_3 + multiples_of_5 - multiples_of_15


if __name__ == '__main__':
    number_of_tests = get_int_input()
    for a0 in range(number_of_tests):
        n = get_int_input()
        res = handle_test_case(n)
        print(res)
