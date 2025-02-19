# @link Problem definition [[docs/hackerrank/warmup/simple_array_sum.md]]

import logging

LOGGER = logging.getLogger(__name__)


def simpleArraySum(arr: list[int]) -> int:
    acum = 0

    for _, value in enumerate(arr):
        acum += value

    LOGGER.info('Simple Array Sum result: %i', acum)
    return acum
