# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/arrays/crush.md]]

import logging

LOGGER = logging.getLogger(__name__)


def array_manipulation(n: int, queries: list[list[int]]) -> int:

    result = [0] * (n + 1)
    maximum = 0

    for [a, b, k] in queries:

        LOGGER.debug("start -> %s", result)
        for j in range(a, b + 1):
            result[j] += k
            LOGGER.debug("result -> %s", result)

    for value in result:
        maximum = max(value, maximum)

    return maximum
