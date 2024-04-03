# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/recursion_and_backtracking/ctci-recursive-staircase.md]] # noqa
# pylint: enable=line-too-long

from typing import Dict


def step_perms_comput_with_cache(n: int, cache: Dict[int, int]) -> int:
    if 0 <= n <= 2:
        return n
    if n == 3:
        return 4

    result = 0
    for i in range(1, 4):
        if n - i not in cache:
            cache[n - i] = step_perms_comput_with_cache(n - i, cache)

        result += cache[n - i]

    return result


def step_perms(n: int) -> int:
    initial_cache: Dict[int, int] = {}
    return step_perms_comput_with_cache(n, initial_cache) % (10 ** 10 + 7)
