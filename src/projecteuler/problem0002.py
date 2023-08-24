# @link Problem definition [[docs/projecteuler/problem0002.md]]

import logging

LOGGER = logging.getLogger(__name__)


def problem0002(_top: int) -> int:
    i = 0
    last1 = 1
    last2 = 0
    even_sum = 0

    fibo = 0

    while fibo < _top:
        fibo = last2 + last1

        LOGGER.debug("Fibonacci(%d) = %d", i, fibo)

        if 0 == fibo % 2:
            even_sum += fibo

        # next keys:
        last2 = last1
        last1 = fibo
        i += 1

    LOGGER.info('Problem 0002 result: %i', even_sum)

    return even_sum
