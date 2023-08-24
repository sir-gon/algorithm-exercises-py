# @link Problem definition [[docs/projecteuler/problem0001.md]]

import logging

LOGGER = logging.getLogger(__name__)


def problem0001(_top: int) -> int:
    total = 0

    for i in range(0, _top):

        if (i % 3 == 0 or i % 5 == 0):
            LOGGER.debug('Line result: %i', i)
            total += i

    LOGGER.info('Problem 0001 result: %i', total)
    return total
