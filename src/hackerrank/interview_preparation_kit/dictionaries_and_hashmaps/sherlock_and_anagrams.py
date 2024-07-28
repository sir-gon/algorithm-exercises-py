# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/dictionaries_and_hashmaps/sherlock_and_anagrams.md]]

from typing import Dict, List
import math

import logging

LOGGER = logging.getLogger(__name__)


def sherlock_and_anagrams(s_word: str) -> int:

    candidates: Dict[str, List[str]] = {}
    size: int = len(s_word)

    # Calculate all substrings
    for i in range(0, size):
        for j in range(0, size - i):
            substr = s_word[i:size - j]
            LOGGER.debug('i: %i, size: %i, size - j: %i | substr: %s',
                         i, size, size - j, substr)

            # Add substrings to a candidate list.
            # two strings are anagrams if sorted strings are the same.
            anagram_candidate = ''.join(sorted(substr))

            # Append candidates to dictionary by "sorted string" key
            if anagram_candidate in candidates:
                candidates[anagram_candidate].append(substr)
            else:
                candidates[anagram_candidate] = [substr]

    count: int = 0
    # Final Anagram list
    for word in list(candidates):
        quantity_of_anagrams = len(candidates[word])
        k = 2

        if quantity_of_anagrams <= 1:
            del candidates[word]
        else:
            # Binomial coefficient: https://en.wikipedia.org/wiki/Binomial_coefficient
            count += math.factorial(quantity_of_anagrams) // (
                math.factorial(k) * math.factorial(quantity_of_anagrams - k)
            )

    LOGGER.debug('Sherlock_and_anagrams() Filtered candidates %i', count)

    return count
