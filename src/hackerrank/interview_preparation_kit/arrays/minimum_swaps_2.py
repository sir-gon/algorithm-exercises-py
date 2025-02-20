# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/arrays/minimum_swaps_2.md]]

import logging

LOGGER = logging.getLogger(__name__)


def minimumSwaps(group: list[int]) -> int:
    indexed_group = [i - 1 for i in group]

    swaps = 0
    index = 0
    size = len(indexed_group)

    while index < size:
        if indexed_group[index] == index:
            index += 1
        else:
            temp = indexed_group[index]
            indexed_group[index] = indexed_group[temp]
            indexed_group[temp] = temp
            swaps += 1

    return swaps
