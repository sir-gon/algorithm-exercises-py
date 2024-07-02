# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/recursion_and_backtracking/ctci-recursive-staircase.md]] # noqa
# pylint: enable=line-too-long

# Use built-in cache mechanism

from functools import cache


@cache
def step_perms(n_steps: int) -> int:
    # Base cases
    if n_steps == 3:
        return 4
    if 2 >= n_steps >= 0:
        return n_steps

    # Recursion
    result = 0
    for i in range(1, 4):
        result += step_perms(n_steps - i)

    return result
