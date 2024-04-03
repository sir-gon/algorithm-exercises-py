# [Recursion: Davis' Staircase](https://www.hackerrank.com/challenges/ctci-recursive-staircase)

Find the number of ways to get from the bottom of a staircase
to the top if you can jump 1, 2, or 3 stairs at a time.

- Difficulty:  `#medium`
- Category: `#ProblemSolvingIntermediate`

Davis has a number of staircases in his house and he likes to
climb each staircase `1`, `2`, or `3` steps at a time.
Being a very precocious child, he wonders how many ways there
are to reach the top of the staircase.

Given the respective heights for each of the  staircases in his house,
find and print the number of ways he can climb each staircase,
module $10^10 + 7 $ on a new line.

## Example

`n = 5`

The staircase has `5` steps. Davis can step on the following sequences of steps:

```text
1 1 1 1 1
1 1 1 2
1 1 2 1
1 2 1 1
2 1 1 1
1 2 2
2 2 1
2 1 2
1 1 3
1 3 1
3 1 1
2 3
3 2
```

There are `13` possible ways he can take these `5` steps and `13 modulo 10000000007`

## Function Description

Complete the stepPerms function using recursion in the editor below.

stepPerms has the following parameter(s):

- int n: the number of stairs in the staircase

## Returns

int: the number of ways Davis can climb the staircase, modulo 10000000007

## Input Format

The first line contains a single integer, `s`, the number of staircases in his house.
Each of the following `s` lines contains a single integer,
`n`, the height of staircase `i`.

## Constraints

- $ 1 \leq s \leq 5 $
- $ 1 \leq n \leq 36 $

## Subtasks

- 1 \leq n \leq 20 for `50%` of the maximum score.

## Sample Input

```text
STDIN   Function
-----   --------
3       s = 3 (number of staircases)
1       first staircase n = 1
3       second n = 3
7       third n = 7
```

## Sample Output

```text
1
4
44
```

## Explanation

Let's calculate the number of ways of climbing
the first two of the Davis' `s = 3` staircases:

1. The first staircase only has `n = 1` step,
    so there is only one way for him to
    climb it (i.e., by jumping `1` step). Thus, we print `1` on a new line.

2. The second staircase has `n = 3` steps and he can climb it in any of the
    four following ways:

    1. 1 -> 1 -> 1
    2. 1 -> 2
    3. 2 -> 1
    4. 3

Thus, we print `4` on a new line.
