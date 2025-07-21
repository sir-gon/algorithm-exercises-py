# [Miscellaneous: Flipping bits](https://www.hackerrank.com/challenges/flipping-bits)

- Difficulty:  `#easy`
- Category: `#ProblemSolvingBasic` `#BitManipulation`

## Using bitwise operations

The bitwise NOT operator (~) flips all bits of the number.

The & 0xFFFFFFFF ensures that we only keep the last 32 bits,
effectively simulating a 32-bit unsigned integer.

This is a more efficient and concise way to achieve the same result
as the original code, without needing to convert to binary strings.
