# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/arrays/crush.md]]

# @see Solution Notes:
# [[docs/hackerrank/interview_preparation_kit/arrays/crush_optimized-solution-notes.md]]

import logging

LOGGER = logging.getLogger(__name__)


def array_manipulation_optimized(n: int, queries: list[list[int]]) -> int:
    # why adding 2?
    #   first slot to adjust 1-based index and
    #   last slot for storing accum_sum result
    result = [0] * (n + 2)
    maximum = 0

    for [a, b, k] in queries:
        # Prefix
        result[a] += k
        result[b + 1] -= k

    accum_sum = 0
    for value in result:
        accum_sum += value
        maximum = max(maximum, accum_sum)

    return maximum
