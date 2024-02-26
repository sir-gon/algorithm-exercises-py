# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/dictionaries_and_hashmaps/sherlock_and_anagrams.md]]

import math


def sherlock_and_anagrams(s: str) -> int:

    candidates = {}
    size = len(s)

    # Calculate all substrings
    for i in range(0, size):
        for j in range(0, size - i):
            substr = s[i:size - j]
            print(f'i: {i}, {size} size - j: {size - j} | substr: {substr}')

            # Add substrings to a candidate list.
            # two strings are anagrams if sorted strings are the same.
            anagram_candidate = ''.join(sorted(substr))

            # Append candidates to dictionary by "sorted string" key
            if anagram_candidate in candidates:
                candidates[anagram_candidate].append(substr)
            else:
                candidates[anagram_candidate] = [substr]

    count = 0
    # Final Anagram list
    for i in list(candidates):
        n = len(candidates[i])
        k = 2

        if len(candidates[i]) <= 1:
            del candidates[i]
        else:
            # Binomial coefficient: https://en.wikipedia.org/wiki/Binomial_coefficient
            count += math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

    print(f'filtered candidates: {count}')

    return count
