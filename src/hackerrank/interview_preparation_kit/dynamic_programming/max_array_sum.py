# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/dynamic_programming/max_array_sum.md]]

def max_array_sum(arr_input: list[int]):
    arr = arr_input[:]

    # Edge case
    if len(arr) == 0:
        return 0

    n = len(arr)

    if n == 1:  # Edge case
        return arr[0]

    # Base case start from index 0 and 1
    t_max = max(arr[0], arr[1])
    arr[1] = t_max

    for i in range(2, n):
        t_max = max(arr[i - 2] + arr[i], t_max)  # Max uptill now
        t_max = max(arr[i], t_max)  # Max in special case where
        # arr[i] + previous max is still less than arr[i]
        # update our inplace array with max for future calculations
        arr[i] = t_max

    return t_max
