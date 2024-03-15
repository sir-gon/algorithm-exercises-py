# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/greedy_algorithms/angry-children.md]] # noqa
# pylint: enable=line-too-long

def max_min(k: int, arr: list[int]):

    sortedlist = sorted(arr[:])
    result = sortedlist[len(arr) - 1] - sortedlist[0]

    for i in range(0, len(arr) - k + 1):
        tmin = sortedlist[i]
        tmax = sortedlist[i + k - 1]
        result = min(result, tmax - tmin)

    return result
