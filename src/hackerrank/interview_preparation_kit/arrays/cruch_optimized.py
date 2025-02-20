# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/arrays/crush.md]]

# @see Solution Notes:
# [[docs/hackerrank/interview_preparation_kit/arrays/crush_optimized-solution-notes.md]]

import logging

LOGGER = logging.getLogger(__name__)


def arrayManipulation(n_operations: int, queries: list[list[int]]) -> int:
    # why adding 2?
    #   first slot to adjust 1-based index and
    #   last slot for storing accum_sum result
    result = [0] * (n_operations + 2)
    maximum = 0

    for [a_start, b_end, k_value] in queries:
        # Prefix
        result[a_start] += k_value
        result[b_end + 1] -= k_value

    accum_sum = 0
    for value in result:
        accum_sum += value
        maximum = max(maximum, accum_sum)

    return maximum
