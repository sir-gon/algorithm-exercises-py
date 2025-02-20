# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/recursion_and_backtracking/recursive-digit-sum.md]] # noqa
# pylint: enable=line-too-long

import sys
sys.set_int_max_str_digits(0)


def superDigitCompute(p_number: int):
    word = str(p_number)

    if len(word) == 1:
        return p_number

    partial = 0
    for digit in word:
        partial += int(digit)

    return superDigitCompute(partial)


def superDigit(n_number: int | str, k_times: int):
    return superDigitCompute(int(n_number) * k_times)
