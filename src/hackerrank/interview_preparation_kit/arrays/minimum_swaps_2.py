# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/arrays/minimum_swaps_2.md]]

import logging

LOGGER = logging.getLogger(__name__)


def minimum_swaps(group: list[int]) -> int:
    q = [i-1 for i in group]

    swaps = 0
    index = 0
    size = len(q)

    while index < size:
        if q[index] == index:
            index += 1
        else:
            temp = q[index]
            q[index] = q[temp]
            q[temp] = temp
            swaps += 1

    return swaps
