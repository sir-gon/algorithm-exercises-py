def count_triplets_brute_force(arr: list[int], r: int) -> int:

    arrc = arr[:]
    arrc = sorted(arrc)
    size = len(arrc)

    counter = 0

    for i in range(0, size - 2):
        for j in range(i + 1, size - 1):
            for k in range(j+1, size):
                print(arrc[i], arrc[j], arrc[k])

                if r * arrc[i] == arrc[j] and r * arrc[j] == arrc[k]:
                    counter += 1

    return counter


def count_triplets_with_cache_and_cuts(arr: list[int], r: int) -> int:

    arrc = arr[:]
    arrc = sorted(arrc)
    size = len(arrc)

    cache: dict[tuple[int, int, int], bool] = {}
    counter = 0

    i_resume = True
    i = 0
    while i < size - 2 and i_resume:
        j_resume = True
        j = i + 1
        while j < size - 1 and j_resume:
            if arrc[j] > r * arrc[i]:
                j_resume = False

            k_resume = True
            k = j + 1
            while k < size and k_resume:
                if arrc[k] > r * arrc[j]:
                    k_resume = False

                triplet = (arrc[i], arrc[j], arrc[k])

                if triplet in cache and cache[triplet]:
                    counter += 1
                else:
                    if r * arrc[i] == arrc[j] and r * arrc[j] == arrc[k]:
                        cache[triplet] = True
                        counter += 1
                    else:
                        cache[triplet] = False

                k += 1
            j += 1
        i += 1

    return counter


def count_triplets(arr: list[int], r: int) -> int:
    pass
