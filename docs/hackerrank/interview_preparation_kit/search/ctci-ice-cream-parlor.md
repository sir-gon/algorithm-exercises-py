# [Search: Hash Tables: Ice Cream Parlor](https://www.hackerrank.com/challenges/ctci-ice-cream-parlor)

- Difficulty:  `#medium`
- Category: `#ProblemSolvingIntermediate` `#search` `#hashtables`

Each time Sunny and Johnny take a trip to the Ice Cream Parlor,
they pool their money to buy ice cream.
On any given day, the parlor offers a line of flavors.
Each flavor has a cost associated with it.

Given the value of `money` and the `cost` of each flavor for `t`
trips to the Ice Cream Parlor, help Sunny and Johnny choose two
distinct flavors such that they spend their entire pool of money during each visit.
ID numbers are the 1-based index number associated with a `cost`.
For each trip to the parlor, print the ID numbers for the two
types of ice cream that Sunny and Johnny purchase as
two space-separated integers on a new line. You must print the smaller
ID first and the larger ID second.

## Example

`cost = [2, 1, 3, 5, 6]``

`money = 5`

They would purchase flavor ID's `1` and `3` for a cost of `2 + 3 = 5`.
Use 1-based indexing for your response.

**Note**:

- Two ice creams having unique IDs  and  may have the same cost
(i.e., $ cost[i] \equiv cost[j] $).

- There will always be a unique solution.

## Function Description

Complete the function whatFlavors in the editor below.

whatFlavors has the following parameter(s):

- `int cost[n]` the prices for each flavor
- `int money`: the amount of money they have to spend

## Prints

- `int int`: the indices of the two flavors they will purchase as
    two space-separated integers on a line

## Input Format

The first line contains an integer, , the number of trips to the ice cream parlor.

Each of the next  sets of  lines is as follows:

- The first line contains `money`.
- The second line contains an integer, `n`, the size of the array `cost`.
- The third line contains `n` space-separated integers denoting the `cost[i]`.

## Constraints

- $ 1 \leq t \leq 50$
- $ 2 \leq money \leq 10^9 $
- $ 2 \leq n \leq 5 * 10^4 $
- $ 1 \leq cost[i] \leq 10^9 $

## Sample Input

```text
STDIN       Function
-----       --------
2           t = 2
4           money = 4
5           cost[] size n = 5
1 4 5 3 2   cost = [1, 4, 5, 3, 2]
4           money = 4
4           cost[] size n = 4
2 2 4 3     cost = [2, 2, 4, 3]
```

## Sample Output

```text
1 4
1 2
```

## Explanation

Sunny and Johnny make the following two trips to the parlor:

1. The first time, they pool together $ money = 4 $ dollars.
    There are five flavors available that day and
    flavors `1` and `4` have a total cost of `1 + 3 = 4`.
2. The second time, they pool together `money = 4` dollars.
    There are four flavors available that day and
    flavors `1` and `2` have a total cost of `2 + 2 = 4`.
