###############################################################################
# Multiples of 3 and 5
#
# https://projecteuler.net/problem=1
#
# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
###############################################################################

import logging

LOGGER = logging.getLogger(__name__)


def problem0000():
    result = 0

    LOGGER.info('Problem 0000 result: %i', result)
    return result
