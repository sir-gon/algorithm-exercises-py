# @link Problem definition [[docs/hackerrank/projecteuler/euler001.md]]
# pylint: disable=C0103:invalid-name

import math


# Function to find sum of Arithmetic Progression series
def sum_of_arithmetic_progression(n: int, d: int) -> int:

    # Number of terms
    n = n // d

    return (n) * (1 + n) * d // 2


# Function to find the sum of all multiples of a and b below n
def euler001(a, b, n) -> int:

    # Since, we need the sum of multiples less than N
    n = n - 1
    lcm = (a * b) // math.gcd(a, b)

    return sum_of_arithmetic_progression(n, a) + \
        sum_of_arithmetic_progression(n, b) - \
        sum_of_arithmetic_progression(n, lcm)
