# [Two Strings](https://www.hackerrank.com/challenges/two-strings)

- Difficulty:  `#easy`
- Category: `#ProblemSolvingBasic` `#dictionaries` `#hashmaps`

Given two strings, determine if they share a common substring.
A substring may be as small as one character.

## Example

`s1 = 'and'`
`s1 = 'art'`

These share the common substring `a`.

`s1 = 'be'`
`s1 = 'cat'`

These do not share a substring.

## Function Description

Complete the function twoStrings in the editor below.

twoStrings has the following parameter(s):

- `string s1`: a string
- `string s2`: another string

## Returns

- `string`: either YES or NO

## Input Format

The first line contains a single integer , the number of test cases.

The following  pairs of lines are as follows:

The first line contains string `s1`.
The second line contains string `s2`.

## Constraints

- `s1` and `s2` consist of characters in the range ascii[a-z].
- $ 1 \leq p \leq 10 $
- $ 1 \leq |s1|, |s2| \leq 10^5 $

## Output Format

For each pair of strings, return `YES` or `NO`.

## Sample Input

```text
2
hello
world
hi
world
```

## Sample Output

```text
YES
NO
```

## Explanation

We have  pairs to check:

1. `s1 = "hello"`, `s2 = "world"`. The substrings `"o"` and `"l"`
are common to both strings.
2. `a = "hi"`, `b = "world"`. `s1` and `s2` share no common substrings.

## Appendix

[Solution notes](two-strings-solution-notes.md)
