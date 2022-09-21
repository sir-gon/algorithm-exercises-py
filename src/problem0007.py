###############################################################################
# 10001st prime
#
# https://projecteuler.net/problem=7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
#
# What is the 10001st prime number?
################################################################################

import logging
from .helpers.prime import is_prime

LOGGER = logging.getLogger(__name__)

def problem0007(_top):

    primes = []

    i = 0
    j = 2
    while len(primes) < _top:
        i += 1

        if is_prime(j):
            primes.append(j)
            LOGGER.debug("Prime found %d put in position: %d", j, len(primes))

        j = 2*i + 1

    answer = primes[len(primes)-1]

    cycles = i

    LOGGER.info("Problem0007 asnwer => %d prime number is: %d in %d", _top, answer, cycles)

    return answer
