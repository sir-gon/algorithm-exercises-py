# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/greedy_algorithms/greedy-florist.md]] # noqa
# pylint: enable=line-too-long


def get_minimum_cost(k_customers: int, c_costs: list[int]):

    flowers = sorted(c_costs[:], reverse=True)
    total: int = 0

    i: int = 0
    for flower_cost in flowers:
        position = i // k_customers

        total += (position + 1) * flower_cost

        i += 1

    return total
