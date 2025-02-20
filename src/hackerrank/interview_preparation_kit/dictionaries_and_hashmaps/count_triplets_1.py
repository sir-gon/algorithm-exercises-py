# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/dictionaries_and_hashmaps/count_triplets_1.md]]

from collections import Counter


def countTripletsBruteForce(arr: list[int], ratio: int) -> int:

    size = len(arr)
    counter = 0

    for i in range(0, size - 2):
        for j in range(i + 1, size - 1):
            for k in range(j + 1, size):
                print(arr[i], arr[j], arr[k])

                if ratio * arr[i] == arr[j] and ratio * arr[j] == arr[k]:
                    counter += 1

    return counter


def countTriplets(arr: list[int], ratio: int) -> int:
    a_counter = Counter(arr)
    b_counter = Counter()
    triplets = 0

    for i in arr:
        j = i // ratio
        k = i * ratio
        a_counter[i] -= 1
        if b_counter[j] and a_counter[k] and i % ratio == 0:
            triplets += b_counter[j] * a_counter[k]
        b_counter[i] += 1

    return triplets
