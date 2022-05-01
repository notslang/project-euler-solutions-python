#!/bin/python3
from euler import get_int_input, is_prime


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


def generate_primes(length):
    """
    Generate a list of primes up to a given length.

    >>> list(generate_primes(6))
    [2, 3, 5, 7, 11, 13]
    """
    prime = 2
    yield prime

    for i in range(1, length):
        prime = get_next_prime(prime)
        yield prime


def handle_test_case(n, primes):
    """
    Handle the test case by finding the nth prime.

    >>> prime_list = list(generate_primes(10000))
    >>> handle_test_case(3, prime_list)
    5
    >>> handle_test_case(6, prime_list)
    13
    >>> handle_test_case(10**4, prime_list)
    104729
    """
    return primes[n - 1]


if __name__ == '__main__':
    number_of_tests = get_int_input()
    prime_list = list(generate_primes(10000))

    for a0 in range(number_of_tests):
        n = get_int_input()
        res = handle_test_case(n, prime_list)
        print(res)
