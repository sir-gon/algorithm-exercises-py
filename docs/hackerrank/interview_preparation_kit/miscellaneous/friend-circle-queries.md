# [Miscellaneous: Friend Circle Queries](https://www.hackerrank.com/challenges/friend-circle-queries)

- Difficulty:  `#medium`
- Category: `#Miscellaneous`

The population of HackerWorld is $ 10^9 $.
Initially, none of the people are friends with each other.
In order to start a friendship, two persons `a` and `b` have to shake hands,
where $ 1 \leq a, b \leq 10^9 $.
The friendship relation is transitive,
that is if `a` and `b` shake hands with each other,
`a` and friends of `b` become friends with `b` and friends of `b`.

You will be given `q` queries. After each query,
you need to report the size of the largest
friend circle (the largest group of friends) formed after considering that query.

For example, your list of queries is:

```text
1 2
3 4
2 3
```

First, `1` and `2` shake hands, forming a circle of `2`.
Next, `3` and `4` do the same. Now there are two groups of `2` friends.
When `2` and `3` become friends in the next query,
both groups of friends are added together to make a circle of `4` friends.
We would print

```text
2
2
4
```

## Function Description

Complete the function maxCircle in the editor below.
It must return an array of integers representing
the size of the maximum circle of friends after each query.

maxCircle has the following parameter(s):

- `queries`: an array of integer arrays,
each with two elements indicating a new friendship

## Input Format

The first line contains an integer, `q`, the number of queries to process.
Each of the next `q` lines consists of two space-separated integers
denoting the 2-D array `queries`.

## Constraints

- $ 1 \leq q \leq 10^5 $
- $ 1
    \leq
    queries[i][0],queries[i][1]
    \leq 10^9
$ for
$ 0 \leq i < q $
- $ queries[i][0] \not = queries[i][1] $

## Output Format

Return an integer array of size `q`,
whose value at index  is the size of
largest group present after processing the $ i^{th}$ query.

## Sample Input 0

```text
2
1 2
1 3
```

## Sample Output 0

```text
2
3
```

## Explanation 0

In the first query, `1` and `2` shake hands.
So, the size of largest group of friends is `2` (as no other friendships exist).
After the second query, `1`, `2` and `3` all become friends,
as `1` shakes hand with `3`, `2` also become friends with `3`
as he was already a friend of `1`.

## Sample Input 1

```text
4
1000000000 23
11 3778
7 47
11 1000000000
```

## Sample Output 1

```text
2
2
2
4
```

## Explanation 1

After first query, person `1000000000` and person `23` become friends.
So, the largest group size is `2`.

After the second query, person `11` and person `3778` become friends.
So, the largest group size is still .

After the third query, person `7` and person `47` become friends.
Answer is still `2`.

After the last query, person `11` and person `1000000000` become friends,
which means `23`, `11`, `1000000000` and `3778` all become friends.
Hence, the answer now increased to `4`.

## Sample Input 2

```text
6
1 2
3 4
1 3
5 7
5 6
7 4
```

## Sample Output 2

```text
2
2
4
4
4
7
```

## Explanation 2

Friend circles after each iteration:

```text
1   [1,2]
2   [1,2],[3,4]
3   [1,2,3,4]
4   [1,2,3,4],[5,7]
5   [1,2,3,4],[5,7,6]
6   [1,2,3,4,5,6,7]
```
