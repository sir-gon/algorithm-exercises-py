# @link Problem definition [[docs/projecteuler/problem0011.md]]

import logging
from .helpers.minmax import maximum

logger = logging.getLogger(__name__)


def problem0011(_square_matrix: list[list[int]], _interval: int) -> int:

    top = len(_square_matrix)
    result = 0

    quadrant_size = _interval
    matrix_limit = len(_square_matrix) - (_interval - 1)

    for i in range(0, matrix_limit):
        if top != len(_square_matrix[i]):
            raise AttributeError("Not a square matrix")

        for j in range(0, matrix_limit):
            logger.debug('start point => i: %i, j: %i', i, j)

            # reset diagonals
            diag1_acum = 1
            diag2_acum = 1
            for k in range(0, quadrant_size):
                logger.debug(
                    'diag1 coordinate: (i, j) = (%i, %i)',
                    i + k,
                    j + k
                )
                logger.debug(
                    'diag2 coordinate: (i, j) = (%i, %i)',
                    i + k,
                    j + (quadrant_size - 1) - k
                )

                diag1_acum *= _square_matrix[i + k][j + k]
                diag2_acum *= _square_matrix[i + k][j + (quadrant_size - 1) - k]
                result = maximum(diag1_acum, result)
                result = maximum(diag2_acum, result)

                # reset lines
                vertical_acum = 1
                horizontal_acum = 1
                for t_l in range(0, quadrant_size):
                    logger.debug(
                        'vertical coordinate: (i, j) = (%i, %i)',
                        i + k,
                        j + t_l
                    )
                    logger.debug(
                        'horizontal coordinate: (i, j) = (%i, %i)',
                        i,
                        j + k
                    )

                    vertical_acum *= _square_matrix[i + k][j + t_l]
                    horizontal_acum *= _square_matrix[i + t_l][j + k]

                    result = maximum(vertical_acum, result)
                    result = maximum(horizontal_acum, result)

    logger.info('Problem 0011 result: %i', result)
    return result
