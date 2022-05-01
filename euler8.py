#!/bin/python3
from euler import get_int_input, get_list_of_ints_input
from math import prod


def generate_sets_of_consecutive_digits(n, number_of_consecutive_digits):
    """
    >>> list(generate_sets_of_consecutive_digits(3675356291, 5))
    ['36753', '67535', '75356', '53562', '35629', '56291']
    """
    digits = str(n)
    length = len(digits)

    for i in range(0, length - number_of_consecutive_digits + 1):
        start_index = i
        end_index = i + number_of_consecutive_digits
        yield digits[start_index:end_index]


def generate_products_of_digits(sets_of_digits):
    """
    >>> list(generate_products_of_digits(["123", "456"]))
    [6, 120]
    """
    for digits in sets_of_digits:
        yield prod([int(d) for d in digits])


def handle_test_case(n, number_of_consecutive_digits):
    """
    Handle the test case.

    >>> handle_test_case(3675356291, 5)
    3150
    >>> handle_test_case(2709360626, 5)
    0
    """
    sets_of_digits = generate_sets_of_consecutive_digits(
        n,
        number_of_consecutive_digits
    )
    return max(generate_products_of_digits(sets_of_digits))


if __name__ == '__main__':
    number_of_tests = get_int_input()
    for a0 in range(number_of_tests):
        number_length, number_of_consecutive_digits = get_list_of_ints_input()
        n = get_int_input()
        res = handle_test_case(n, number_of_consecutive_digits)
        print(res)
