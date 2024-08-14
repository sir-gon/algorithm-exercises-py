# [Linked Lists: Insert a node at a specific position in a linked list](https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list)

- Difficulty:  `#easy`
- Category: `#ProblemSolvingIntermediate` `#linkedlists`

Given the pointer to the head node of a linked list and an integer
to insert at a certain position, create a new node with the given
integer as its `data` attribute, insert this node at the desired
position and return the head node.

A position of `0` indicates head, a position of `1` indicates one
node away from the head and so on.
The head pointer given may be null meaning that the initial list is empty.

## Example

`head` refers to the first node in the list `1 -> 2 -> 3`
`data = 4`
`position = 2`

Insert a node at position `2` with `data = 4`.
The new list is `1 -> 2 -> 3 -> 4`

## Function Description

Complete the function `insertNodeAtPosition` in the editor below.
It must return a reference to the head node of your finished list.

insertNodeAtPosition has the following parameters:

- head: a SinglyLinkedListNode pointer to the head of the list
- data: an integer value to insert as data in your new node
- position: an integer position to insert the new node, zero based indexing

## Returns

SinglyLinkedListNode pointer: a reference to the head of the revised list

## Input Format

The first line contains an integer `n`, the number of elements in the linked list.

Each of the next `n` lines contains an integer `SinglyLinkedListNode[i].data`.
The next line contains an integer `data`, the data of the node that is to be inserted.
The last line contains an integer `position`.

## Constraints

- $ 1 \leq n \leq 1000 $
- $ 1 \leq $ `SinglyLinkedListNode[i].data` $ \leq 1000 $,
where `SinglyLinkedListNode[i]` is the $ {i}\th $ element of the linked list.
- $ 0 \leq position \leq n $

## Sample Input

```text
3
16
13
7
1
2
```

## Sample Output

```text
16 13 1 7
```

## Explanation

The initial linked list is `16 -> 13 -> 7`.
Insert `1` at the position `2` which currently has `7` in it.
The updated linked list is `16 -> 13 -> 1 -> 7`.
