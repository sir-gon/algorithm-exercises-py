# @link Problem definition [[docs/projecteuler/problem0021.md]]

###############################################################################
# Result found: 31626
# Amicable numbers found:
# amicableNumbers [
#      '220',  '284',
#      '1184', '1210',
#      '2620', '2924',
#      '5020', '5564',
#      '6232', '6368'
#    ]
###############################################################################

import logging
from .helpers.natural_number import NaturalNumber

LOGGER = logging.getLogger(__name__)


def problem0021(_start: int, _limit: int) -> int:
    proper_divisors_of = {}

    for i in range(_start, _limit):
        proper_divisors_of[i] = sum(NaturalNumber(i).proper_divisors())

    amicable_numbers = []

    for index, value in proper_divisors_of.items():
        if (index in proper_divisors_of
                and value in proper_divisors_of
                and index != value
                and index == proper_divisors_of[value]):

            amicable_numbers.append(index)

    result = sum(amicable_numbers)

    LOGGER.info('Problem 0021 result: %i', result)
    return result
