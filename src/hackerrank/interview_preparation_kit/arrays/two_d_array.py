# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/arrays/two_d_array.md]]

import logging

LOGGER = logging.getLogger(__name__)


def gethourglass(arr: list[list[int]], position_x: int, position_y: int) -> list[int]:
    result: list[int] = []

    # top
    result.append(arr[position_x - 1][position_y - 1])
    result.append(arr[position_x - 1][position_y])
    result.append(arr[position_x - 1][position_y + 1])

    # middle
    result.append(arr[position_x][position_y])

    # bottom
    result.append(arr[position_x + 1][position_y - 1])
    result.append(arr[position_x + 1][position_y])
    result.append(arr[position_x + 1][position_y + 1])

    return result


def hourglass_sum(arr: list[list[int]]) -> int | None:
    matrix_size: int = len(arr)

    matrix_start_index: int = 1
    matrix_stop_index: int = matrix_size - 1

    max_hourglass_sum: int | None = None

    for i in range(matrix_start_index, matrix_stop_index):
        for j in range(matrix_start_index, matrix_stop_index):

            houglass_values: list[int] = gethourglass(arr, i, j)
            this_hourglass_sum: int = sum(houglass_values)

            if max_hourglass_sum is None or this_hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = this_hourglass_sum

    return max_hourglass_sum
