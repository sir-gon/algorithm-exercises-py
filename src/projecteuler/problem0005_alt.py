# @link Problem definition [[docs/projecteuler/problem0005.md]]

import math
import logging
from .lib.natural_number import NaturalNumber

LOGGER = logging.getLogger(__name__)


def _increase(element: int, group: dict[int, int]) -> dict[int, int]:
    elem = group.get(element, None)
    if elem is None:
        group.update({element: 1})
    else:
        group.update({element: elem + 1})

    return group


def _replace_maximum(element: int, count: int, group: dict[int, int]) -> dict[int, int]:
    elem = group.get(element, None)
    if elem is None:
        group.update({element: count})
    else:
        group.update({element: count if count > elem else elem})

    return group


def prime_factors_collection(factors: list[int]) -> dict[int, int]:
    collection = {}

    for factor in factors:
        collection = _increase(factor, collection)

    return collection


def problem0005_alt(_bottom: int, _top: int) -> 'None | float':

    minimum_prime_factors = {}
    result: None | float = None

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
