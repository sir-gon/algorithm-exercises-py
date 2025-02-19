# pylint: disable=line-too-long
# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/greedy_algorithms/minimum-absolute-difference-in-an-array.md]]
# pylint: enable=line-too-long

import logging

LOGGER = logging.getLogger(__name__)


def minimumAbsoluteDifference(arr: list[int]) -> int | None:
    sorted_nums = sorted(arr)
    result = None

    for i in range(len(sorted_nums) - 1):
        a_value = sorted_nums[i]
        b_value = sorted_nums[i + 1]

        diff = abs(a_value - b_value)

        if result is None:
            result = diff
        else:
            result = min(result, diff)

    return result
