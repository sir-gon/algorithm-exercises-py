# [The Fibonacci Sequence](https://www.hackerrank.com/challenges/ctci-fibonacci-numbers)

- Difficulty:  `#easy`
- Category: `#ProblemSolvingBasic`

## The Fibonacci Sequence

The Fibonacci sequence appears in nature all around us,
in the arrangement of seeds in a sunflower and the spiral of a nautilus for example.

The Fibonacci sequence begins with `fibonacci(0) = 0` and `fibonacci(1) = 1`
as its first and second terms. After these first two elements,
each subsequent element is equal to the sum of the previous two elements.

Programmatically:

- `fibonacci(0) = 0`
- `fibonacci(1) = 1`
- `fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)`

Given , return the  number in the sequence.

## Example

The Fibonacci sequence to `6` is `fs = [0, 1, 1, 2, 3, 5, 8]`.
With zero-based indexing, `fs[5] = 5`.

## Function Description

Complete the recursive function `fibonacci` in the editor below.

fibonacci has the following parameter(s):

- `int n`: the index of the sequence to return

## Returns

- `int`: the  element in the Fibonacci sequence

## Input Format

The integer `n`.

## Constraints

- $ 0 \leq n \leq 30 $

## Sample Input

```text
STDIN   Function
-----   --------
3       n = 3
```

## Sample Output

```text
2
```

## Explanation

The Fibonacci sequence begins as follows:

```C
fibonacci(0) = 0
fibonacci(1) = 1
fibonacci(2) = (0 + 1) = 1
fibonacci(3) = (1 + 1) = 2
fibonacci(4) = (1 + 2) = 3
fibonacci(5) = (2 + 3) = 5
fibonacci(6) = (3 + 5) = 8
```

...

In the sequence above, `fibonacci(3)` is `2`.
