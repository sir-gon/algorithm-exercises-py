###############################################################################
# Summation of primes
#
# https:##projecteuler.net/problem=10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
###############################################################################

## ############################################################################
## About solution: BRUTE FORCE
##
## Found:
## ...
## Prime found 1999969 put in position: 148931
## Prime found 1999979 put in position: 148932
## Prime found 1999993 put in position: 148933
## Sum of primes below 2000000 is: 142913828922
##
## ############################################################################

import logging

from src.helpers.natural_number import NaturalNumber

LOGGER = logging.getLogger(__name__)


def problem0010(_top_limit):
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
