# @link Problem definition [[docs/hackerrank/warmup/a_very_big_sum.md]]

import logging

LOGGER = logging.getLogger(__name__)


def a_very_big_sum(_input: list[int]) -> int:
    result: int = 0

    for i in _input:
        result += i

    LOGGER.info('A Very Big Sum result: %i', result)
    return result
