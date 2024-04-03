# [Recursion: Davis' Staircase](https://www.hackerrank.com/challenges/ctci-recursive-staircase)

Find the number of ways to get from the bottom of a staircase
to the top if you can jump 1, 2, or 3 stairs at a time.

- Difficulty:  `#medium`
- Category: `#ProblemSolvingIntermediate`

## Failed solution

This solution correctly calculates the result. The problem is its performance,
since due to the traversal of the recursion tree,
it is eventually easy to reach repeated cases that are recalculated each time.

```python
def step_perms_compute(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    return \
        step_perms_compute(n - 3) + \
        step_perms_compute(n - 2) + \
        step_perms_compute(n - 1)
```

## Alternative solution

The final solution introduces a simple caching mechanism,
so that repeated cases are not recalculated.

The trade-off is that the algorithm now requires
more memory to run in less time.
