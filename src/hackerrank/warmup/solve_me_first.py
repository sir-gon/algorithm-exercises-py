# @link Problem definition [[docs/hackerrank/warmup/solve_me_first.md]]

import logging

LOGGER = logging.getLogger(__name__)


def solve_me_first(_a: int, _b: int) -> int:
    result = _a + _b

    LOGGER.info('Solve Me First result: %i', result)
    return result
