###############################################################################
# Smallest multiple
#
# https://projecteuler.net/problem=5
#
# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by
# all of the numbers from 1 to 20?
###############################################################################

import math
import logging
from .helpers.natural_number import NaturalNumber

LOGGER = logging.getLogger(__name__)

def _increase(element, group: dict):
    elem = group.get(element, None)
    if elem is None:
        group.update({element: 1})
    else:
        group.update({element: elem + 1})

    return group

def _replace_maximum(element, count, group: dict):
    elem = group.get(element, None)
    if elem is None:
        group.update({element: count})
    else:
        group.update({element: count if count > elem else elem })

    return group

def prime_factors_collection(factors: list):
    collection = {}

    for factor in factors:
        collection = _increase(factor, collection)

    return collection

def problem0005_alt(_bottom, _top):

    minimum_prime_factors = {}
    result = None

    cycles = 0

    for i in range(_bottom, _top + 1):

        number = NaturalNumber(i)
        primes = number.prime_factors()
        cycles += number.get_prime_factors_cycles()

        factors = prime_factors_collection(primes)
        cycles += len(primes)

        LOGGER.debug('Prime Factors of %d list    => %s', i, str(primes))
        LOGGER.debug('Prime Factors of %d grouped => %s', i, str(factors))

        for factor, quantity in factors.items():
            cycles += 1
            _replace_maximum(factor, quantity, minimum_prime_factors)

        LOGGER.debug('Prime Factors of %d grouped => %s', i, str(minimum_prime_factors))

    result = 1

    for factor, quantity in minimum_prime_factors.items():
        cycles += 1
        result *= math.pow(factor, quantity)

    LOGGER.info('Problem 0005: %d in %d cycles', result, cycles)
    return result
