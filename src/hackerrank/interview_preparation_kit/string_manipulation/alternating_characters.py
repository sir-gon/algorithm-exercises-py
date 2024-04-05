# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/string_manipulation/alternating-characters.md]] # noqa
# pylint: enable=line-too-long

def alternating_characters(s: str):

    last: str = ''
    new_string: str = ''

    for x in s:
        if x != last:
            new_string += x

        last = x

    return len(s) - len(new_string)
