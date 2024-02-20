# [Array Manipulation](https://www.hackerrank.com/challenges/crush)

Perform m operations on an array and print the maximum of the values.

- Difficulty:  ` #hard `
- Category: ` #ProblemSolvingIntermediate `

## Solution sources

### Brute force idea

The first solution attempt is based on the idea of going through:

>     -> each row and then,
>         -> each sub-set of elements affected by the operation.

With this principle, the algorithm becomes O(N^2)

### Optimized

Reading about posible optimizations,
I found the possibility of summarizing the interior traversal with
addition operations for each element in each row of operations,
in only 2 constant operations, which represents the necessary values so that
in a single final traversal, the sum values can be obtained "by drag".
The algorithm is called "prefix sum."

Some sources about "prefix sum"

- <https://hmn.wiki/en/Prefix_sum>
- <https://en.wikipedia.org/wiki/Prefix_sum>
- <https://usaco.guide/silver/prefix-sums?lang=py>

Some sources about implementation in:

- [HackerRank Array Manipulation — beat the clock using Prefix Sum (JavaScript)](https://medium.com/@mlgerardvla/hackerrank-array-manipulation-beat-the-clock-using-prefix-sum-92471060035e)
- [Hackerrank Discussions Forums: Array Manipulation](https://www.hackerrank.com/challenges/one-month-preparation-kit-crush/forum)
