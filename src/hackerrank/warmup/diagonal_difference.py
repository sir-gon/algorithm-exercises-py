# @link Problem definition [[docs/hackerrank/warmup/diagonal_difference.md]]

import logging

LOGGER = logging.getLogger(__name__)


def diagonalDifference(arr: list[list[int]]) -> int:
    diag1 = 0
    diag2 = 0
    last = len(arr) - 1

    for i, line in enumerate(arr):
        for j, cell in enumerate(line):
            if i == j:
                diag1 += cell
                diag2 += arr[last - i][j]

    result = abs(diag1 - diag2)

    LOGGER.info('Diagonal Difference result: %i', result)
    return result
