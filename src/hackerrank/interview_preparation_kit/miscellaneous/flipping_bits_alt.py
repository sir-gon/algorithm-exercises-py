# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/miscellaneous/flipping-bits.md]] # noqa
# @see Solution Notes: [[docs/hackerrank/interview_preparation_kit/miscellaneous/flipping-bits-alt-solution-notes.md]] # noqa
# pylint: enable=line-too-long

def flippingBitsAlt(number: int) -> int:
    return ~number & 0xFFFFFFFF
