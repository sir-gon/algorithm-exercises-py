# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/recursion_and_backtracking/recursive-digit-sum.md]] # noqa
# pylint: enable=line-too-long

import sys
sys.set_int_max_str_digits(0)


def super_digit_compute(p_number: int):
    word = str(p_number)

    if len(word) == 1:
        return p_number

    partial = 0
    for digit in word:
        partial += int(digit)

    return super_digit_compute(partial)


def super_digit(n_number: int | str, k_times: int):
    return super_digit_compute(int(n_number) * k_times)
