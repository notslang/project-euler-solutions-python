#!/bin/python3
from euler import get_int_input


def handle_test_case(n):
    """
    Handle the test case.

    >>> handle_test_case(4)
    -1
    >>> handle_test_case(12)
    60
    """
    triple_products = []
    for a in range(1, n):
        b = ((a * a) - (a - n) ** 2) // (2 * (a - n))
        c = n - a - b
        if a < b < c and (a * a + b * b == c * c):
            triple_products.append(a * b * c)

    if len(triple_products) == 0:
        return -1
    else:
        return max(triple_products)


if __name__ == '__main__':
    number_of_tests = get_int_input()

    for a0 in range(number_of_tests):
        n = get_int_input()
        res = handle_test_case(n)
        print(res)
