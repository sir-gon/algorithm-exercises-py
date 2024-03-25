# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/search/ctci-ice-cream-parlor.md]] # noqa
# pylint: enable=line-too-long

def what_flavors(cost, money) -> list[int] | None:

    cache = {}

    for i, x in enumerate(cost):
        diff = money - x

        if diff in cache:
            return sorted([i + 1, cache[diff] + 1])

        cache[x] = i

    return None
