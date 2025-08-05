# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/miscellaneous/ctci-big-o.md]] # noqa
# pylint: enable=line-too-long

import math


# pylint: disable=duplicate-code
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
# pylint: enable=duplicate-code


def primality(n):
    return "Prime" if primeFactor(n) == n else "Not prime"
