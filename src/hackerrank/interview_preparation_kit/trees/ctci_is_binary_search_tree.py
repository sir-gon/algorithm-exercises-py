# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/trees/ctci-is-binary-search-tree.md]] # noqa
# pylint: enable=line-too-long

from ...lib.node import Node


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


def traverse_bst(node: Node | None, collect: list[int]) -> list[int] | None:
    if node is not None:
        traverse_bst(node.left, collect)

        collect.append(node.data)

        traverse_bst(node.right, collect)


def check_bst(root: Node | None) -> bool:
    plaint_tree = []
    traverse_bst(root, plaint_tree)
    print(plaint_tree)

    result = True
    nodes_count = len(plaint_tree)

    if nodes_count > 1:
        last = plaint_tree[0]
        for i in range(1, nodes_count):
            if plaint_tree[i] < last:
                return False

            last = plaint_tree[i]

    return result
