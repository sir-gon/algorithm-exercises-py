# Problem definition
# [[docs/hackerrank/interview_preparation_kit/dictionaries_and_hashmaps/two-strings.md]]

__YES__ = 'Yes'
__NO__ = 'No'


def twoStringsCompute(s1_word: str, s2_word: str) -> bool:
    for letter in s1_word:
        if letter in s2_word:
            return True

    return False


def twoStrings(s1_word: str, s2_word: str) -> str:
    return __YES__ if twoStringsCompute(s1_word, s2_word) else __NO__
