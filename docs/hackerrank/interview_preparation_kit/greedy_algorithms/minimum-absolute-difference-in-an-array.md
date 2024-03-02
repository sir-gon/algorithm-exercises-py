# [Minimum Absolute Difference in an Array](https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array)

- Difficulty:  `#medium`
- Category: `#ProblemSolvingBasic`

The absolute difference is the positive difference between two
values `a` and `b`, is written $ \lvert a - b \rvert $
or $ \lvert b - a \rvert $
and they are equal. If `a = 3` and `b = 2`, $ \lvert 3 - 2 \rvert =
\lvert 2 - 3 \rvert = 1 $.
Given an array of integers, find the minimum absolute difference
between any two elements in the array.

**Example** `arr = [-2, 2, 4]`6

There are  pairs of numbers: `[-2, 2]`, `[-2, 4]` and `[2, 4]`.
The absolute differences for these pairs are
$ \lvert (-2) - 2 \rvert = 4 $, $ \lvert (-2) - 4 \rvert = 6 $ and
$ \lvert 2 - 4 \rvert = 2 $.
The minimum absolute difference is `2`.

## Function Description

Complete the minimumAbsoluteDifference function in the editor below.
It should return an integer that represents the minimum absolute difference
between any pair of elements.

minimumAbsoluteDifference has the following parameter(s):

- `int arr[n]`: an array of integers

## Returns

int: the minimum absolute difference found

## Input Format

The first line contains a single integer , the size of .
The second line contains  space-separated integers, .

## Constraints

- $ 2 \leq n \leq 10^5 $
- $ -10^9 \leq arr[i] \leq 10^9 $

## Sample Input 0

```text
3
3 -7 0
```

## Sample Output 0

```text
3
```

## Explanation 0

The first line of input is the number of array elements. The array,
 `arr = [3, -7, 0]`
There are three pairs to test: `(3, -7)`, `(3, 0)`, and `(-7, 0)`.
The absolute differences are:

- $ \lvert 3 - -7 \rvert => 10 $
- $ \lvert 3 - 0 \rvert => 3 $
- $ \lvert -7 - 0 \rvert => 7 $

Remember that the order of values in
the subtraction does not influence the result.
The smallest of these absolute differences is `3`.

## Sample Input 1

```text
10
-59 -36 -13 1 -53 -92 -2 -96 -54 75
```

## Sample Output 1

```text
1
```

## Explanation 1

The smallest absolute difference is $ \lvert - 54 - -53 \rvert = 1$.

## Sample Input 2

```text
5
1 -3 71 68 17
```

## Sample Output 2

```text
3
```

## Explanation 2

The minimum absolute difference is $ \lvert - 71 - 68 \rvert = 3$.
