#!/bin/python3
from euler import get_int_input


def fib_generator(ceiling):
    """
    Generate a fibonacci sequence.
    """
    term1 = 1
    term2 = 2

    if term1 < ceiling:
        yield term1

    if term2 < ceiling:
        yield term2

    while True:
        res = term1 + term2
        if res < ceiling:
            term1 = term2
            term2 = res
            yield res
        else:
            return


def handle_test_case(n):
    """
    Handle the test case.

    >>> handle_test_case(10)
    10
    >>> handle_test_case(100)
    44
    """
    total = 0
    for i in fib_generator(n):
        if i % 2 == 0:
            total += i
    return total


if __name__ == '__main__':
    number_of_tests = get_int_input()
    for a0 in range(number_of_tests):
        n = get_int_input()
        res = handle_test_case(n)
        print(res)
