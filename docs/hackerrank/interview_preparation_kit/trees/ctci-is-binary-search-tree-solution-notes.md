# [Trees: Is This a Binary Search Tree?](https://www.hackerrank.com/challenges/ctci-is-binary-search-tree)

- Difficulty:  `#medium`
- Category: `#ProblemSolvingAdvanced`

## How to get test case structures

Code to dump tree structures from examples:

```python
if root is not None:
    left = None
    if(root.left is not None):
        left = root.left.data
    right = None
    if(root.right is not None):
        right = root.right.data
    print(f"parent: {root.data} | left: {left} | right: {right}")
```

## Failed tries

This solution is based on the idea of locally checking the
properties of the binary tree,
that the value of the left side is less than the current value
and the right side is greater than the current side.

The problem is that the local analysis does not take into account
the values of higher nodes of the same branch,
and it also does not check the case of duplicate elements.

```python
def check_bst_failed_try(root: Node | None) -> bool:
    if root is not None:
        left = None
        if root.left is not None:
            left = root.left.data
        right = None
        if root.right is not None:
            right = root.right.data
        print(f"parent: {root.data} | left: {left} | right: {right}")

    if root is None:
        return True

    if root.left is not None and root.left.data > root.data:
        return False

    if root.right is not None and root.right.data < root.data:
        return False

    return check_bst_failed_try(root.left) and check_bst_failed_try(root.right)
```

## Working solution

The solution is based on the idea of doing an "in-order"
traversal of the tree (recursively) and collecting the values in a list.

As a second step, it is verified that the elements are
ordered ascending and that they are strictly different from the previous one.

If a value were repeated at non-contiguous points in the list,
the order property would not be satisfied.
