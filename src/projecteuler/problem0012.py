# @link Problem definition [[docs/projecteuler/problem0012.md]]

import logging
from .helpers.natural_number import NaturalNumber

LOGGER = logging.getLogger(__name__)


def problem0012(_top: int) -> int:
    amount_of_divisors = 0
    triangular = 0
    i = 1

    while amount_of_divisors < _top:
        triangular += i
        number = NaturalNumber(triangular)

        list_of_divisors = number.divisors()
        amount_of_divisors = len(list_of_divisors)

        LOGGER.debug("Triangular number: %i has %i divisors",
                     triangular, amount_of_divisors)

        i += 1

    LOGGER.info('Problem 0012 result: %i', triangular)
    return triangular
