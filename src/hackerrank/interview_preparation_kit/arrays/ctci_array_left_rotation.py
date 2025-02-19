# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/arrays/ctci_array_left_rotation.md]]

import logging

LOGGER = logging.getLogger(__name__)
FIRST_POSITION: int = 0


def rotLeftOne(group: list[int]) -> list[int]:

    first = group.pop(FIRST_POSITION)
    group.append(first)

    return group


def rotLeft(group: list[int], d_rotations: int) -> list[int]:

    output = group.copy()
    i = 1
    while i <= d_rotations:
        output = rotLeftOne(output)
        i += 1

    return output
