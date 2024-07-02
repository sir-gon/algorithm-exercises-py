# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/search/ctci-ice-cream-parlor.md]] # noqa
# pylint: enable=line-too-long

def what_flavors(cost: list[int], money: int) -> list[int] | None:

    cache = {}

    for i, price in enumerate(cost):
        diff = money - price

        if diff in cache:
            return sorted([i + 1, cache[diff] + 1])

        cache[price] = i

    return None
