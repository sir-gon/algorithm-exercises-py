# Brute force

def what_flavors_brute_force(cost, money):

    for i, x in enumerate(cost):

        budget = money - x

        for j in range(i + 1, len(cost)):
            if budget - cost[j] == 0:
                print(f'{i + 1} {j + 1}')
                return [i + 1, j + 1]

    return []


# binary search
def what_flavors(cost, money):

    flavors = []
    for index, i in enumerate(cost):
        flavors.append({
            'index': index,
            'value': i
        })
    flavors.sort(key=lambda item: item['value'])

    for i, x in enumerate(flavors):
        budget = money - x['value']

        left: int = 0
        right: int = len(flavors) - 1
        center: int = len(flavors) // 2

        while right - left > 1:
            if budget == flavors[center]['value']:
                return sorted([i + 1, flavors[center]['index'] + 1])

            if budget < flavors[center]['value']:
                # left conservates
                right = center

            if budget > flavors[center]['value']:
                left = center
                #

            center = left + (right - left) // 2

    return []
