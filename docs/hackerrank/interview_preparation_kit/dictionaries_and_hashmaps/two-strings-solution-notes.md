# [Two Strings](https://www.hackerrank.com/challenges/two-strings)

- Difficulty:  `#easy`
- Category: `#ProblemSolvingBasic` `#dictionaries` `#hashmaps`

## Clarification

The problem asks to find if there is a substring between 2 words,
it does not require finding a particular one that meets a certain property,
not counting all the possible ones.

With that in mind, simply find the first 1-letter intersection between two word
to return "YES".
The worst case is to return "NO" after going through both words letter by letter.
