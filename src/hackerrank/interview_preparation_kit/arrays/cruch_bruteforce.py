# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/arrays/crush.md]]

import logging

LOGGER = logging.getLogger(__name__)


def arrayManipulation(n_operations: int, queries: list[list[int]]) -> int:
    result = [0] * (n_operations + 1)
    maximum = 0

    for [a_start, b_end, k_value] in queries:

        LOGGER.debug("start -> %s", result)
        for i in range(a_start, b_end + 1):
            result[i] += k_value
            LOGGER.debug("result -> %s", result)

    for value in result:
        maximum = max(value, maximum)

    return maximum
