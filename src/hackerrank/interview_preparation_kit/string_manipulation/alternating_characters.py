# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/string_manipulation/alternating-characters.md]] # noqa
# pylint: enable=line-too-long

def alternating_characters(word: str) -> int:

    last: str = ''
    new_string: str = ''

    for letter in word:
        if letter != last:
            new_string += letter

        last = letter

    return len(word) - len(new_string)
