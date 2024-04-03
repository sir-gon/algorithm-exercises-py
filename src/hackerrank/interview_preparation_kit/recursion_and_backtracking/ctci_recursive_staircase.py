# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/recursion_and_backtracking/ctci-recursive-staircase.md]] # noqa
# pylint: enable=line-too-long

def step_perms_compute(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    return \
        step_perms_compute(n - 3) + \
        step_perms_compute(n - 2) + \
        step_perms_compute(n - 1)


def step_perms(n):
    return step_perms_compute(n) % (10 ** 10 + 7)
