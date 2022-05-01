#!/bin/python3
from euler import get_int_input


def is_palindrome(string):
    # if the first char is not the same as the last, it is not a palindrome
    if string[0] != string[-1]:
        return False

    length = len(string)

    # any 1 char string is a palindrome
    # any 2 char string with the same first / last chars is a palindrome
    if length == 1 or length == 2:
        return True

    # it's a longer string, check the middle
    return is_palindrome(string[1:-1])


def is_palindromic_number(number):
    """
    Break a number up into a tuple containing at most two factors. If the number
    is prime then return only it in a tuple.

    >>> is_palindromic_number(101101)
    True
    >>> is_palindromic_number(1)
    True
    >>> is_palindromic_number(42)
    False
    >>> is_palindromic_number(793397)
    True
    """

    return is_palindrome(str(number))


def three_digit_product_generator(ceiling):
    # find all the products of two 3 digit numbers less than ceiling
    for a in range(100, 999):
        for b in range(100, a):
            product = a * b
            if product < ceiling:
                yield product
            else:
                break


def palindrome_generator(ceiling):
    for product in three_digit_product_generator(ceiling):
        if is_palindromic_number(product):
            yield product


def get_palindromes():
    return sorted(palindrome_generator(1000000), reverse=True)


def handle_test_case(n, palindromes):
    """
    Handle the test case.

    >>> palindromes = get_palindromes()
    >>> handle_test_case(101110, palindromes)
    101101
    >>> handle_test_case(800000, palindromes)
    793397
    >>> handle_test_case(1000000, palindromes)
    906609
    """
    for p in palindromes:
        if p < n:
            return p


if __name__ == '__main__':
    number_of_tests = get_int_input()
    palindromes = get_palindromes()

    for a0 in range(number_of_tests):
        n = get_int_input()
        res = handle_test_case(n, palindromes)
        print(res)
