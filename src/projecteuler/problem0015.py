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
