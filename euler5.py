#!/bin/python3
from euler import get_int_input


def is_divisible_by_range(number, a, b):
    for divisor in range(b, a - 1, -1):
        if number % divisor != 0:
            return False

    return True


def handle_test_case(n):
    """
    Handle the test case.

    >>> handle_test_case(3)
    6
    >>> handle_test_case(10)
    2520
    """
    test_number = 1

    while True:
        if is_divisible_by_range(test_number, 1, n):
            return test_number

        test_number += 1


if __name__ == '__main__':
    number_of_tests = get_int_input()
    for a0 in range(number_of_tests):
        n = get_int_input()
        res = handle_test_case(n)
        print(res)
