#!/bin/python3
from euler import get_int_input, get_next_prime


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
