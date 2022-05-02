import sys
from math import sqrt, floor


def get_int_input(): return int(input().strip())


def get_list_of_ints_input():
    inputs = input().strip().split()
    return list(map(lambda x: int(x), inputs))


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


def is_prime(number):
    """
    Checks if a number is prime.

    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(15)
    False
    >>> is_prime(200)
    False
    >>> is_prime(209)
    False
    >>> is_prime(25)
    False
    >>> is_prime(104729)
    True
    >>> is_prime(179424673)
    True
    """
    return number != 1 and len(factorize(number)) == 1


def get_next_prime(number):
    """
    Find the next prime that comes after a given number.

    >>> get_next_prime(0)
    2
    >>> get_next_prime(1)
    2
    >>> get_next_prime(4)
    5
    >>> get_next_prime(104723)
    104729
    """
    if number == 1 or (number % 2 == 0 and number != 0):
        # primes above 2 cannot be even and 1 isn't a prime
        number += 1
    else:
        # don't return the same number if given a prime
        number += 2

    # as of 2017-10-02, the largest known prime gap is 1510, so this loop will
    # probably never run more than 755 times for the inputs we're giving it.
    while not is_prime(number):
        # 2 is the smallest prime gap, and all prime gaps other than the gap
        # between 2 & 3 are even.
        number += 2
    return number
