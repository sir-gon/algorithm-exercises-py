# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/miscellaneous/maximum-xor.md]] # noqa
# pylint: enable=line-too-long

def maxXor(arr: list[int], queries: list[int]) -> list[int]:
    result = []

    for j in queries:
        maximum = 0
        for x in arr:
            maximum = max(maximum, j ^ x)
        result.append(maximum)

    return result
