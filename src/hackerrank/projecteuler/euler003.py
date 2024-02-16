# @link Problem definition [[docs/hackerrank/projecteuler/euler003.md]]
# pylint: disable=C0103:invalid-name

def prime_factor(n: int) -> 'int | None':

    if n < 2:
        return None

    divisor = n
    max_prime_factor = 2

    i = 2
    while i <= divisor:
        if 0 == divisor % i:
            max_prime_factor = i
            divisor = int(divisor / i)
        else:
            i += 1

    return max_prime_factor


def euler003(n: int) -> 'int | None':

    return prime_factor(n)
