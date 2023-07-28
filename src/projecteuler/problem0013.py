import logging

LOGGER = logging.getLogger(__name__)


def problem0013(_array_of_numbers: list[int], _firts_digits: int):

    sum_of_big_numbers = sum(_array_of_numbers)
    sum_of_big_numbers = str(sum_of_big_numbers)[0:_firts_digits]
    sum_of_big_numbers = int(sum_of_big_numbers)

    LOGGER.info('Problem 0013 result: %i', sum_of_big_numbers)
    return sum_of_big_numbers
