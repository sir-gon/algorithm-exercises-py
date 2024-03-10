# [Dictionaries and Hashmaps: Count Triplets](https://www.hackerrank.com/challenges/count-triplets-1)

- Difficulty:  `#medium`
- Category: `#ProblemSolvingIntermediate`

## Failed tries

### Introducing optimizations and cache

This solution is based on the idea of traversing each possible case,
similar to brute force, but introducing a cache mechanism
for each case found and cutting the number of times it would have to be traversed.

This has following problems:

1) The problem is that it preserves the complexity of O(n^3) (same as brute force)

2) "Cognitive Complexity" (measured by sonarlint) it is very high.
This due to the number of nesting.

3) Initially, the innermost calculation assumes that the values in the array
"should" be ordered, that is, it expects that the values to the right of the
currently evaluated value would be larger.
With this idea in mind, an initial ordering of values was introduced.
But the problem requires that the values be in positions i < j < k.
That is why initially an ordering of the input was executed,
but such ordering introduces unexpected possibilities. In an unordered list,
it can produce overcounts of favorable cases.

```python
def count_triplets_with_cache_and_cuts(arr: list[int], r: int) -> int:

    # arrc = arr[:]
    # arrc = sorted(arrc)
    size = len(arr)

    cache: dict[tuple[int, int, int], bool] = {}
    counter = 0

    i_resume = True
    i = 0
    while i < size - 2 and i_resume:
        j_resume = True
        j = i + 1
        while j < size - 1 and j_resume:
            if arr[j] > r * arr[i]:
                j_resume = False

            k_resume = True
            k = j + 1
            while k < size and k_resume:
                if arr[k] > r * arr[j]:
                    k_resume = False

                triplet = (arr[i], arr[j], arr[k])

                if triplet in cache and cache[triplet]:
                    counter += 1
                else:
                    if r * arr[i] == arr[j] and r * arr[j] == arr[k]:
                        cache[triplet] = True
                        counter += 1
                    else:
                        cache[triplet] = False

                k += 1
            j += 1
        i += 1

    return counter
```

### Reducing complexity

This solutions reduce complexity to O(N), but has the same problem
with unordered lists as the previous case.

```python
def count_triplets_doenst_work_with_unsorted_input(arr: list[int], r: int) -> int:
    count: int = 0

    if len(arr) < 3:
        return count

    counter = Counter(arr)
    size = len(counter)
    limit = size - 2

    i = 0
    for k, v in counter.items():
        knext = k * r
        knext_next = k * r * r

        if i < limit and knext in counter and knext_next in counter:
            next_elem_cnt = counter[knext]
            next_next_elem_cnt = counter[knext_next]
            count += v * (next_elem_cnt * next_next_elem_cnt)
        elif r == 1:
            count += math.factorial(v) // (math.factorial(3) * math.factorial(v - 3))

        i += 1

    return count
```

## Working solution

This solution in O(N), is based on considering that each
number analyzed is in the center of the triplet and asks
"how many" possible cases there are on the left and
right to calculate how many possible triplets are formed.

- Source: [Hackerrank - Count Triplets Solution](https://www.thepoorcoder.com/hackerrank-count-triplets-solution/)
