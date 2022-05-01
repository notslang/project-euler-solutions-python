#!/bin/python3
from euler import get_int_input, factorize


def prime_factor_generator(n):
    while True:
        factors = factorize(n)

        if len(factors) == 2:
            prime_factor, n = factors
            yield prime_factor
        else:
            yield factors[0]
            break


def handle_test_case(n):
    """
    Handle the test case.

    >>> handle_test_case(10)
    5
    >>> handle_test_case(17)
    17
    """
    return max(prime_factor_generator(n))


if __name__ == '__main__':
    number_of_tests = get_int_input()
    for a0 in range(number_of_tests):
        n = get_int_input()
        res = handle_test_case(n)
        print(res)
