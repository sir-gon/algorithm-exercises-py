# [Greedy Algorithms: Greedy Florist](https://www.hackerrank.com/challenges/greedy-florist)

- Difficulty:  `#medium`
- Category: `#ProblemSolvingBasic` `#greedyalgorithms`

## About the problem statement

At first it seems a bit confusing. Due the problem statement tends to
make us believe that the most convenient thing is to start with the highest
numbers, but the examples doesn't not present a logical descending order.

## Way of thinking

After rereading the problem several times it can be determined that:

- It does not matter who the buyers are, nor in what order they buy,
nor how much each one buys.
The important thing is how many people are organized
into a group to minimize the purchase price.

- If the number of people in the group is greater than or equal to
the number of different flowers, then the price is the lowest possible,
because they can all be purchased "in a single pass",
making each person in the group (or less) buy 1 unit.

- The price of flowers does matter, therefore it is more convenient to buy
the most expensive ones first.
Each "round" of purchasing makes the flowers more expensive,
therefore it is better to buy the cheapest ones in the last "round."

## Deductions

- It seems convenient to sort the flower price list entry in descending order
(or in ascending order, traversing the new sorted list in reverse).

- The number of passes depends on how many "groups" of "k - people"
fit in the list of flowers, that is:
$ \textbf{\#(c) / k}$ (integer division)

- At first I assumed that the order in which the traversal is done in
the examples was a suggestion of the criteria in which the list of flowers
should be traversed to reach the solution.

    Finally, realizing that the price calculation in descending order
    (and "the round" in which the purchase is made)
    and the example were equivalent, made me consider the idea that the order of
    the examples might just be a distractor,
    introduced on purpose to make deducing the solution a little more difficult.
