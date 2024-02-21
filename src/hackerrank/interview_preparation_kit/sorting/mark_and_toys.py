# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/sort/mark-and-toys.md]]

def maximum_toys(prices: list[int], k: int):

    group = prices[:]
    group.sort()

    budget = k
    shopping_cart = []

    while 0 < len(group) and budget >= 0:
        current_item = group.pop(0)
        budget -= current_item
        if budget >= 0:
            shopping_cart.append(current_item)

    return len(shopping_cart)
