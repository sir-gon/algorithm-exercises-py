# [Arrays: Minimum Swaps 2](https://www.hackerrank.com/challenges/minimum-swaps-2)

Return the minimum number of swaps to sort the given array.

- Difficulty:  `#medium`
- Category: `#ProblemSolvingIntermediate` `#arrays`

You are given an unordered array consisting of consecutive integers
[1, 2, 3, ..., n] without any duplicates. You are allowed to swap any
two elements. Find the minimum number of swaps required to sort the
array in ascending order.

## Example

` arr = [7, 1, 3, 2, 4, 5, 6] `

Perform the following steps:

```text
i   arr                     swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]
```

It took `5` swaps to sort the array.

## Function Description

Complete the function minimumSwaps in the editor below.

minimumSwaps has the following parameter(s):

- `int arr[n]`: an unordered array of integers

## Returns

- `int`: the minimum number of swaps to sort the array

## Input Format

The first line contains an integer, , the size of .
The second line contains  space-separated integers .

## Constraints

Sample Input 0

- $ 1 \leq n \leq 10^5 $
- $ 1 \leq arr[i] \leq 10^5 $

## Sample Input 0

```text
4
4 3 1 2
```

## Sample Output 0

```text
3
```

## Explanation 0

Given array `arr: [4, 3, 1, 2]`

After swapping `(0, 2)` we get `[1, 3, 4, 2]`

After swapping `(1, 2)` we get `[1, 4, 3, 2]`

After swapping `(1, 3)` we get `[1, 2, 3, 4]`

So, we need a minimum of `3` swaps to sort the array in ascending order.

## Sample Input 1

```text
5
2 3 4 1 5
```

## Sample Output 1

```text
3
```

## Explanation 1

Given array `arr: [1, 3, 5, 2, 4, 6, 7]`

After swapping `(1, 3)` we get `[2, 3, 1, 4, 5]`

After swapping `(0, 1)` we get `[3, 2, 1, 4, 5]`

After swapping `(0, 2)` we get `[1, 2, 3, 4, 5]`

So, we need a minimum of `3` swaps to sort the array in ascending order.

## Sample Input 2

```text
7
1 3 5 2 4 6 7
```

## Sample Output 2

```text
3
```

## Explanation 2

Given array `[1, 3, 5, 2, 4, 6, 7]`

After swapping `(1, 3)` we get `[1, 2, 5, 3, 4, 6, 7]`

After swapping `(2, 3)` we get `[1, 2, 3, 5, 4, 6, 7]`

After swapping `(3, 4)` we get `[1, 2, 3, 4, 5, 6, 7]`

So, we need a minimum of `3` swaps to sort the array in ascending order.
