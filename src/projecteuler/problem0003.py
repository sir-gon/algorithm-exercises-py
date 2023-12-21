# @link Problem definition [[docs/projecteuler/problem0003.md]]

import logging
from .lib.natural_number import NaturalNumber

LOGGER = logging.getLogger(__name__)


def problem0003(_top: int) -> 'None | int':

    number = NaturalNumber(_top)
    prime_factors = number.prime_factors()
    LOGGER.debug('Prime factors of %d: %s', _top, prime_factors)

    prime_factors.sort()

    max_prime_factor = prime_factors[len(prime_factors) - 1]

    LOGGER.info('Problem 0003 result: %d', max_prime_factor)
    return max_prime_factor
