# [Strings: Alternating Characters](https://www.hackerrank.com/challenges/alternating-characters)

- Difficulty:  `#easy`
- Category: `#ProblemSolvingBasic` `#strings`

You are given a string containing characters `A` and `B` only.
Your task is to change it into a string such that there are
no matching adjacent characters.
To do this, you are allowed to delete zero or more
characters in the string.

Your task is to find the minimum number of required deletions.

## Example

`s = AABAAB`

Remove an at `A` positions `0` and `3` to make `s = ABAB` in `2` deletions.

## Function Description

Complete the alternatingCharacters function in the editor below.
alternatingCharacters has the following parameter(s):

- `string s`: a string

## Returns

- `int`: the minimum number of deletions required

## Input Format

The first line contains an integer `q`, the number of queries.
The next `q` lines each contain a string `s` to analyze.

## Constraints

- $ 1 \leq q \leq 10 $
- $ 1 \leq lenght of  s \leq 10^5 $
- Each string `s` will consist only of characters `A` and `B`.

## Sample Input

```text
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB
```

## Sample Output

```text
3
4
0
0
4
```

## Explanation

The characters marked red are the ones that can be deleted
so that the string does not have matching adjacent characters.

```text
AAAA => A, 3 deletions
BBBBB => B, 4 deletions
ABABABAB => ABABABAB, 0 deletions
BABABA => BABABA, 0 deletions
AAABBB => AB, 4 deletions
```
