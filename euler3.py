#!/bin/python3

import sys
from math import sqrt, floor


def get_int_input(): return int(input().strip())


def factorize(number):
    """
    Break a number up into a tuple containing at most two factors. If the number
    is prime then return only it in a tuple.

    >>> factorize(1)
    (1,)
    >>> factorize(2)
    (2,)
    >>> factorize(3)
    (3,)
    >>> factorize(5)
    (5,)
    >>> factorize(7)
    (7,)
    >>> factorize(9)
    (3, 3)
    >>> factorize(4)
    (2, 2)
    >>> factorize(2 * 3 * 7)
    (2, 21)
    >>> factorize(197 * 251)
    (197, 251)
    >>> factorize(100)
    (2, 50)
    >>> factorize(15485917 * 23879549)
    (15485917, 23879549)
    """
    # handle the only even prime, first odd prime, and 1
    if number is 3 or number is 2 or number is 1:
        return number,

    # test the only even prime first, this lets us reduce the values of
    # `possible_factor` that we test by half
    if number % 2 is 0:
        return 2, number // 2

    # test the first odd prime first, this lets us reduce the values of
    # `possible_factor` that we test by about 1/3rd
    if number % 3 is 0:
        return 3, number // 3

    square_root = sqrt(number)

    # so long as we've calculated the square root, we might as well see if it's
    # a valid factor. this is a constant-time test, so no big deal.
    if square_root.is_integer():
        square_root = int(square_root)
        return square_root, square_root

    # check for larger factors, we only need to test up to the square root of
    # the number, since you could never have a factor larger than that. We add
    # to possible_factor in a pattern alternating between +2 and +4, resulting
    # in a possible_factor list like 5, 7, 11, 13, 17, 19, 23, 25. This lets us
    # easily skip all the multiples of 2 and all the multiples of 3. To do this
    # without a counter, we increment by 6 for each loop, and check both
    # possible_factor and possible_factor + 2.
    for possible_factor in range(5, floor(square_root) + 1, 6):
        # we are technically able to use `is` here since zero is mapped to a
        # fixed location in memory. this gives us significantly more speed.
        if number % possible_factor is 0:
            return possible_factor, number // possible_factor

        if number % (possible_factor + 2) is 0:
            return possible_factor + 2, number // (possible_factor + 2)

    return number,


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
