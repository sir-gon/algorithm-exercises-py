# pylint: disable=C0200:consider-using-enumerate
# pylint: disable=C0103:invalid-name

import logging
from typing import List

LOGGER = logging.getLogger(__name__)


def validCoordinate(grid: List[List[int]], i: int, j: int, k: int, m: int) -> bool:
    return 0 <= k < len(grid) and \
        0 <= m < len(grid[k]) and \
        (k, m) != (i, j)


def allNeighborsAreMinor(grid: List[List[int]], i: int, j: int) -> bool:
    for k in range(i - 1, i + 2):
        for m in range(j - 1, j + 2):
            if validCoordinate(grid, i, j, k, m) and \
                    grid[k][m] >= grid[i][j]:
                LOGGER.debug(
                    'Found some major neighbor: i = %i, j = %i, grid[i][j] = %i',
                    k,
                    m,
                    grid[k][m]
                )
                return True

    return False


def numCells(grid: List[List[int]]) -> int:

    dominant_counter = 0

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            LOGGER.debug('Checking: i = %i, j = %i, grid[i][j] = %i', i, j, grid[i][j])

            if allNeighborsAreMinor(grid, i, j) is False:
                LOGGER.debug('grid[%i][%i] is dominant', i, j)
                dominant_counter += 1

    return dominant_counter
