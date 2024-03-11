# Problem definition
# [[docs/hackerrank/interview_preparation_kit/dictionaries_and_hashmaps/two-strings.md]]

__YES__ = 'Yes'
__NO__ = 'No'


def two_strings_compute(s1: str, s2: str) -> bool:
    for x in s1:
        if x in s2:
            return True

    return False


def two_strings(s1: str, s2: str) -> str:
    return __YES__ if two_strings_compute(s1, s2) else __NO__
