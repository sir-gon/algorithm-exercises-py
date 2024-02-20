# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/arrays/crush.md]]

import logging

LOGGER = logging.getLogger(__name__)


def array_manipulation(n: int, queries: list[list[int]]) -> int:

    result = [0] * n

    for row in queries:

        start = row[0] - 1
        end = row[1]
        k = row[2]

        LOGGER.debug("start -> %s", result)
        for j in range(start, end):
            result[j] += k
            LOGGER.debug("result -> %s", result)

    maximum = None
    for value in result:
        if maximum is None or value > maximum:
            maximum = value

    return maximum or 0
