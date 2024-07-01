# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/recursion_and_backtracking/ctci-recursive-staircase.md]] # noqa
# pylint: enable=line-too-long

from typing import Dict


def step_perms_comput_with_cache(n_steps: int, cache: Dict[int, int]) -> int:
    if 0 <= n_steps <= 2:
        return n_steps
    if n_steps == 3:
        return 4

    result = 0
    for i in range(1, 4):
        if n_steps - i not in cache:
            cache[n_steps - i] = step_perms_comput_with_cache(n_steps - i, cache)

        result += cache[n_steps - i]

    return result


def step_perms(n_steps: int) -> int:
    initial_cache: Dict[int, int] = {}
    return step_perms_comput_with_cache(n_steps, initial_cache) % (10 ** 10 + 7)
