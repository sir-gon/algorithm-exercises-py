###############################################################################
# Sum square difference
#
# https://projecteuler.net/problem=6
#
# The sum of the squares of the first ten natural numbers is,
#
# 1² * 2² * ... * 10² = 385
#
# The square of the sum of the first ten natural numbers is,
#
# (1 * 2 * ... * 10)² = 3025
#
# Hence the difference between the sum of the squares of the
# first ten natural numbers and the square of the sum is
# 3025 - 385.
#
# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.
################################################################################

import math
import logging

LOGGER = logging.getLogger(__name__)


def problem0006(_bottom: int, _top: int):
    answer = 0

    sum_of_squares = 0
    base_for_square_of_sum = 0
    square_of_sum = 0

    for i in range(_bottom, _top +1):
        sum_of_squares += math.pow(i, 2)
        base_for_square_of_sum += i

    square_of_sum = math.pow(base_for_square_of_sum, 2)

    answer = square_of_sum - sum_of_squares

    LOGGER.debug('Sum of first %i squares = %i', _top, sum_of_squares)
    LOGGER.debug(
        'Base for Square Of Sum of first %i = %i',
        _top,
        base_for_square_of_sum
    )
    LOGGER.debug('Square Of Sum of first %i = %i',
        _top,
        square_of_sum
    )

    LOGGER.info('Problem 0006 result: %i', answer)
    return answer
