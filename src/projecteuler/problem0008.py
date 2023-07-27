import logging
from .helpers.product import product

LOGGER = logging.getLogger(__name__)


def problem0008(_number, _interval):

    digits = list(_number)
    top = len(digits)
    bottom = 0
    maximum = 0

    for i in range(bottom, top - _interval + 1):

        digit_set = []

        for j in range(0, _interval):
            digit_set.append(digits[i + j])

        partial = product(digit_set)
        maximum = max(partial, maximum)

    LOGGER.info('Problem 0008: %s', maximum)

    return maximum
