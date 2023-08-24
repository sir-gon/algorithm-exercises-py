# @link Problem definition [[docs/projecteuler/problem0006.md]]

import math
import logging

LOGGER = logging.getLogger(__name__)


def problem0006(_bottom: int, _top: int) -> float:
    answer = 0

    sum_of_squares = 0
    base_for_square_of_sum = 0
    square_of_sum = 0

    for i in range(_bottom, _top + 1):
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
    LOGGER.debug(
        'Square Of Sum of first %i = %i',
        _top,
        square_of_sum
    )

    LOGGER.info('Problem 0006 result: %i', answer)
    return answer
