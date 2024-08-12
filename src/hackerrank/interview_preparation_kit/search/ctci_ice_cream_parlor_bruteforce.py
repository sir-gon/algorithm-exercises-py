def what_flavors_brute_force(cost: list[int], money: int) -> list[int] | None:

    for i, x in enumerate(cost):

        budget = money - x

        for j in range(i + 1, len(cost)):
            if budget - cost[j] == 0:
                print(f'{i + 1} {j + 1}')
                return [i + 1, j + 1]

    return None
