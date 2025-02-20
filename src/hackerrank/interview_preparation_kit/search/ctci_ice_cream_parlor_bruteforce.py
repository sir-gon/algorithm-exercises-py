def whatFlavors(cost: list[int], money: int) -> list[int] | None:

    for i, price in enumerate(cost):

        budget = money - price

        for j in range(i + 1, len(cost)):
            if budget - cost[j] == 0:
                print(f'{i + 1} {j + 1}')
                return [i + 1, j + 1]

    return None
