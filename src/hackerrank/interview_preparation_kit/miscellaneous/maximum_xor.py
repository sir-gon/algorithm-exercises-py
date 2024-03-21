def max_xor(arr, queries):

    result = []

    for j in queries:
        maximum = 0
        for x in arr:
            maximum = max(maximum, j ^ x)
        result.append(maximum)

    return result
