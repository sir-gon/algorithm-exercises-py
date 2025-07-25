# [Miscellaneous: Maximum Xor](https://www.hackerrank.com/challenges/maximum-xor)

- Difficulty:  `#medium`
- Category: `#Miscellaneous`

Find the maximum xor value in the array.

You are given an array `arr` of `n` elements.
A list of integers, `queries` is given as an input,
find the maximum value of
`queries[j]` $ \oplus $ `each arr[i]`
for all $ 0 \leq i < n $,
where \oplus represents [xor](https://en.wikipedia.org/wiki/Exclusive_or)
of two elements.

Note that there are multiple test cases in one input file.

For example:

$ \begin{array}{ll}
arr &= [3, 7, 15, 10] \\
queries[j] &= 3 \\
\end{array} $

$ \begin{array}{l:l}
  3 \oplus 3 = 0 & max = 0 \\
  3 \oplus 7 = 4 & max = 4 \\
  3 \oplus 15 = 12 & max = 12 \\
  3 \oplus 10 = 9 & max = 12 \\
\end{array} $

## Function Description

Complete the maxXor function in the editor below.
It must return an array of integers,
each representing the maximum xor value for each element `queries[j]`
against all elements of `arr`.

maxXor has the following parameter(s):

- arr: an array of integers
- queries: an array of integers to query

## Input Format

The first line contains an integer `n`, the size of the array `arr`.

The second line contains `n` space-separated integers,
`arr[i]` from $ 0 \leq i < n $.

The third line contain `m`, the size of the array `queries`.

Each of the next `m` lines contains an
integer `queries[j]` where $ 0 \leq j < m $.

## Constraints

- $ 1 \leq n,m \leq 10^5 $
- $ 0 \leq arr[i], queries[j] \leq 10^9 $

## Output Format

The output should contain `m` lines with each line representing output
for the corresponding input of the testcase.

## Sample Input 0

```text
3
0 1 2
3
3
7
2
```

## Sample Output 0

```text
3
7
3
```

## Explanation 0

$ arr = [0, 1, 2] $

$ queries[0] = 3 $

$ \begin{array}{l:l}
  3 \oplus 0 = 3 & max = 3 \\
  3 \oplus 1 = 2 & max = 3 \\
  3 \oplus 2 = 1 & max = 3 \\
\end{array} $

$ queries[1] = 7 $

$ \begin{array}{l:l}
  7 \oplus 0 = 7 & max = 7 \\
  7 \oplus 1 = 6 & max = 7 \\
  7 \oplus 2 = 5 & max = 7 \\
\end{array} $

$ queries[2] = 2 $

$ \begin{array}{l:l}
  2 \oplus 0 = 2 & max = 3 \\
  2 \oplus 1 = 3 & max = 3 \\
  2 \oplus 2 = 0 & max = 3 \\
\end{array} $

## Sample Input 1

```text
5
5 1 7 4 3
2
2
0
```

## Sample Output 1

```text
7
7
```

## Explanation 1

$ arr = [5, 1, 7, 4, 3] $

$ queries[0] = 2 $

$ \begin{array}{l:l}
  2 \oplus 5 = 7 & max = 7 \\
  2 \oplus 1 = 3 & max = 7 \\
  2 \oplus 7 = 5 & max = 7 \\
  2 \oplus 4 = 7 & max = 7 \\
  2 \oplus 3 = 3 & max = 7 \\
\end{array} $

$ queries[1] = 7 $

$ \begin{array}{l:l}
  0 \oplus 5 = 7 & max = 7 \\
  0 \oplus 1 = 3 & max = 7 \\
  0 \oplus 7 = 5 & max = 7 \\
  0 \oplus 4 = 7 & max = 7 \\
  0 \oplus 3 = 3 & max = 7 \\
\end{array} $

## Sample Input 2

```text
4
1 3 5 7
2
17
6
```

## Sample Output 2

```text
22
7
```

## Explanation 2

$ arr = [1, 2, 5, 7] $

$ queries[0] = 17 $

$ \begin{array}{l:l}
  17 \oplus 16 = 16 & max = 16 \\
  17 \oplus 18 = 18 & max = 18 \\
  17 \oplus 20 = 20 & max = 20 \\
  17 \oplus 22 = 22 & max = 22 \\
\end{array} $

$ queries[1] = 6 $

$ \begin{array}{l:l}
  6 \oplus 7 = 7 & max = 7 \\
  6 \oplus 5 = 5 & max = 7 \\
  6 \oplus 3 = 3 & max = 7 \\
  6 \oplus 1 = 1 & max = 7 \\
\end{array} $
