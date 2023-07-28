import logging
from .helpers.minmax import maximum

logger = logging.getLogger(__name__)


def problem0011(_square_matrix: list[list[int]], _interval: int) -> int:

    top = len(_square_matrix)
    result = 0
    acum = 0

    for i in range(0, top):
        if top != len(_square_matrix[i]):
            raise AttributeError("Not a square matrix")

        for j in range(0, top):
            logger.debug('i: %i, j: %i', i, j)

            acum = 1

            if i < top - (_interval - 1):
                logger.debug('---- VERTICAL ------------------------------------------')
                # vertical

                for k in range(0, _interval):
                    logger.debug(
                      'row: i %i, column: %i, step %i => %i',
                      i + k, j, k, _square_matrix[i + k][j]
                      )

                    acum *= _square_matrix[i + k][j]

            result = maximum(acum, result)

            acum = 1
            if j < top - (_interval - 1):
                logger.debug('---- HORIZONTAL ----------------------------------------')
                # horizontal
                for k in range(0, _interval):
                    logger.debug(
                      'row: i %i, column: %i, step %i => %i',
                      i, j + k, k, _square_matrix[i][j + k]
                      )
                    acum *= _square_matrix[i][j + k]

            result = maximum(acum, result)

            acum = 1
            if i + (_interval - 1) < top and j + (_interval - 1) < top:
                # diagonal top left -> bottom right
                logger.debug('---- DIAG \\ ---------------------------------------------')
                for k in range(0, _interval):
                    logger.debug(
                            'row: i %i, column: %i, step %i => %i',
                            i + k, j + k, k, _square_matrix[i + k][j + k]
                    )
                    acum *= _square_matrix[i + k][j + k]

            result = maximum(acum, result)

            acum = 1
            if i + (_interval - 1) < top and j + (_interval - 1) < top:
                # diagonal top rigth -> bottom left
                logger.debug('---- DIAG / ---------------------------------------------')
                for k in range(0, _interval):
                    logger.debug(
                        'row: i %i, column: %i, step %i => %i',
                        i + k,
                        j + (_interval - 1) - k,
                        _interval,
                        _square_matrix[i + k][j + (_interval - 1) - k]
                    )
                    acum *= _square_matrix[i + k][j + (_interval - 1) - k]

            result = maximum(acum, result)

    logger.info('Problem 0011 result: %i', result)
    return result
