###############################################################################
# Lattice paths
#
# https://projecteuler.net/problem=15
#
#
# Starting in the top left corner of a 2×2 grid, and only being able to move
# to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?
################################################################################

import logging
from .helpers.matrix import matrix

LOGGER = logging.getLogger(__name__)


def problem0015(_grid_side: int = 20):
    vertex_matrix = matrix(_grid_side + 1, _grid_side + 1, 1)

    for i in range(1, _grid_side + 1):
        for j in range(1, _grid_side + 1):
            upper_parent = vertex_matrix[i - 1][j]
            left_parent = vertex_matrix[i][j - 1]

            vertex_matrix[i][j] = upper_parent + left_parent

    LOGGER.info('Paths found %d', vertex_matrix[_grid_side][_grid_side])
    LOGGER.debug('Matrix: %s', vertex_matrix)
    return vertex_matrix[_grid_side][_grid_side]
