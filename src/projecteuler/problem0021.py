###############################################################################
# Amicable numbers
#
# https://projecteuler.net/problem=21
#
# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
#
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are
# an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10,
# 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
#
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10021.
#
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
