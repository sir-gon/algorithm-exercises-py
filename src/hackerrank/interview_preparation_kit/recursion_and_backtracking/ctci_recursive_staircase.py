# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/recursion_and_backtracking/ctci-recursive-staircase.md]] # noqa
# @see Solution Notes: [[docs/hackerrank/interview_preparation_kit/recursion_and_backtracking/ctci-recursive-staircase-solution-notes.md]] # noqa
# pylint: enable=line-too-long

from typing import Dict

TOP_LIMIT = 10 ** 10 + 7
STEPS_LIMIT = 3


def step_perms_comput_with_cache(
        n_steps: int,
        cache: Dict[int, int],
        steps_limit: int) -> int:

    # Base cases
    if 0 <= n_steps <= 2:
        return n_steps

    result = 0
    for i in range(1, min(steps_limit, n_steps) + 1):
        search_key: int = n_steps - i

        if search_key not in cache:
            cache[search_key] = step_perms_comput_with_cache(
                search_key,
                cache,
                steps_limit
            )

        result += cache[search_key]

    return (result + 1) if n_steps <= steps_limit else result


def step_perms(n_steps: int) -> int:
    initial_cache: Dict[int, int] = {}
    return step_perms_comput_with_cache(n_steps, initial_cache, STEPS_LIMIT) % TOP_LIMIT
