# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/dictionaries_and_hashmaps/count_triplets_1.md]]

from collections import Counter


def count_triplets_brute_force(arr: list[int], r: int) -> int:

    size = len(arr)
    counter = 0

    for i in range(0, size - 2):
        for j in range(i + 1, size - 1):
            for k in range(j + 1, size):
                print(arr[i], arr[j], arr[k])

                if r * arr[i] == arr[j] and r * arr[j] == arr[k]:
                    counter += 1

    return counter


def count_triplets(arr, r):
    a_counter = Counter(arr)
    b_counter = Counter()
    triplets = 0

    for i in arr:
        j = i // r
        k = i * r
        a[i] -= 1
        if b[j] and a[k] and i % r == 0:
            triplets += b[j] * a[k]
        b[i] += 1

    return triplets
