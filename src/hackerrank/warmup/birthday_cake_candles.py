# @link Problem definition [[docs/hackerrank/warmup/birthday_cake_candles.md]]

import logging

LOGGER = logging.getLogger(__name__)


def birthdayCakeCandles(_ar: list[int]) -> int:
    if len(_ar) == 0:
        raise ValueError('Empty input')

    counter: int = 0
    maximum: int = _ar[0]

    for element in _ar:
        if element > maximum:
            maximum = element
            counter = 1
        else:
            if element == maximum:
                counter += 1

    LOGGER.info('Birthday Cake Candles result: %i', counter)
    return counter
