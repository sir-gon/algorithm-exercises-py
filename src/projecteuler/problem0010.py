# @link Problem definition [[docs/projecteuler/problem0010.md]]

# ############################################################################
# About solution: BRUTE FORCE
#
# Found:
# ...
# Prime found 1999969 put in position: 148931
# Prime found 1999979 put in position: 148932
# Prime found 1999993 put in position: 148933
# Sum of primes below 2000000 is: 142913828922
#
# ############################################################################

import logging

from .lib.natural_number import NaturalNumber

LOGGER = logging.getLogger(__name__)


def problem0010(_top_limit: int) -> int:
    primes = []
    i = 2

    while i <= _top_limit:
        test_number = NaturalNumber(i)
        if test_number.is_prime():
            primes.append(i)
            LOGGER.info('Prime found %i put in position: %i', i, len(primes))
        i += 1

    result = sum(primes)
    LOGGER.info('Problem 0010 result: %i', result)
    return result
