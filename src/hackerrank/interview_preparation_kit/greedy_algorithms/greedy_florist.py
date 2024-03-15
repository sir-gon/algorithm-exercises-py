# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/greedy_algorithms/greedy-florist.md]] # noqa
# pylint: enable=line-too-long


def get_minimum_cost(k: int, c: list[int]):

    flowers = sorted(c[:], reverse=True)
    total: int = 0

    i: int = 0
    for x in flowers:
        j = i // k

        total += (j + 1) * x

        i += 1

    return total
