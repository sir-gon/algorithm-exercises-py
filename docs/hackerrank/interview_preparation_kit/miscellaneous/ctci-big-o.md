# [Time Complexity: Primality](https://www.hackerrank.com/challenges/ctci-big-o)

- Difficulty:  `#medium`
- Category: `#ProblemSolvingBasic`

## Using bitwise operations

A prime is a natural number greater than `1` that has no positive divisors other
than `1` and itself.
Given `p` integers, determine the primality of each integer and return `Prime`
or `Not prime` on a new line.

**Note**: If possible, try to come up with an $ \mathcal{O}(\sqrt{n}) $
primality algorithm, or see what sort of optimizations you can come up with for
san $ \mathcal{O}(\sqrt{n}) $ algorithm. Be sure to check out the Editorial
after submitting your code.

## Function Description

Complete the primality function in the editor below.
primality has the following parameter(s):

- `int` n: an integer to test for primality

## Returns

- string: Prime if  is prime, or Not prime

## Input Format

The first line contains an integer, , the number of integers to check for primality.
Each of the  subsequent lines contains an integer, , the number to test.

## Constraints

- $ 1 \leq p \leq 30 $
- $ 1 \leq n \leq 2 × 10^9 $

## Sample Input

```text
STDIN   Function
-----   --------
3       p = 3 (number of values to follow)
12      n = 12 (first number to check)
5       n = 5
7       n = 7
```

## Sample Output

```text
Not prime
Prime
Prime
```

## Explanation

We check the following $ p = 3 $ integers for primality:

1. $ n = 12 $ is divisible by numbers other than $ 1 $ and itself
  (i.e.: $ 2 $, $ 3 $, $ 4 $, $ 6 $).
1. $ n = 5 $ is only divisible  and itself.
1. $ n = 7 $ is only divisible  and itself.
