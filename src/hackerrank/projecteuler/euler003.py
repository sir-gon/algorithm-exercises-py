# @link Problem definition [[docs/hackerrank/projecteuler/euler003.md]]
# pylint: disable=C0103:invalid-name
#
# Notes about final solution please see
# @link [[docs/hackerrank/projecteuler/euler003-solution-notes.md]]
import math


def primeFactor(n: int) -> 'int | None':

    if n < 2:
        return None

    divisor = n
    max_prime_factor = None

    i = 2
    while i <= math.sqrt(divisor):
        if 0 == divisor % i:
            divisor = int(divisor / i)
            max_prime_factor = divisor
        else:
            i += 1

    if max_prime_factor is None:
        return n

    return max_prime_factor


def euler003(n: int) -> 'int | None':

    return primeFactor(n)
