# pylint: disable=line-too-long
# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/greedy_algorithms/minimum-absolute-difference-in-an-array.md]]
# pylint: enable=line-too-long

import logging

LOGGER = logging.getLogger(__name__)


def minimum_absolute_difference(arr: list[int]) -> int | None:
    sorted_nums = sorted(arr)
    result = None

    for i in range(len(sorted_nums) - 1):
        a = sorted_nums[i]
        b = sorted_nums[i + 1]

        diff = abs(a - b)

        if result is None:
            result = diff
        else:
            result = min(result, diff)

    return result
