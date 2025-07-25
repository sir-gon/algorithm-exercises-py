# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/miscellaneous/maximum-xor.md]] # noqa
# pylint: enable=line-too-long

def maxXor(arr: list[int], queries: list[int]) -> list[int]:
    max_dict: dict[int, int] = {}
    result = []

    for j in queries:

        if j in max_dict:
            result.append(max_dict[j])
        else:
            maximum: int = 0
            for x in arr:
                maximum = max(maximum, j ^ x)
            max_dict[j] = maximum
            result.append(maximum)

    return result
