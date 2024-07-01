# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/sort/ctci-bubble-sort.md]]

from __future__ import annotations
import logging

LOGGER = logging.getLogger(__name__)
SEPARATOR = "\n"


# pylint: disable=R0903:too-few-public-methods
class SortableGroup:
    group: list[int]
    count: int

    def __init__(self, group: list[int]):
        self.count = 0
        self.group = group

    def bubble_sort(self) -> SortableGroup:

        group = self.group[:]  # copy original list

        n = len(group)
        count = 0
        i = 0

        while i < n:

            for j in range(0, len(group) - 1):

                if group[j] > group[j + 1]:
                    temp = group[j]
                    group[j] = group[j + 1]
                    group[j + 1] = temp
                    count += 1
            i += 1

        self.count = count
        self.group = group

        return self


def count_swaps(group: list[int]) -> str:

    sortable_group = SortableGroup(group)
    sortable_group.bubble_sort()

    last = len(sortable_group.group) - 1

    output = f'Array is sorted in {sortable_group.count} swaps.{SEPARATOR}' + \
             f'First Element: {sortable_group.group[0]}{SEPARATOR}' + \
             f'Last Element: {sortable_group.group[last]}{SEPARATOR}'

    return output
