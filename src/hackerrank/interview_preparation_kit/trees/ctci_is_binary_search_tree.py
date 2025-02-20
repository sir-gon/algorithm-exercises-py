# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/trees/ctci-is-binary-search-tree.md]] # noqa
# pylint: enable=line-too-long

from ...lib.node import Node


def traverseBST(root: Node | None, collect: list[int]) -> list[int] | None:
    if root is not None:
        traverseBST(root.left, collect)

        collect.append(root.data)

        traverseBST(root.right, collect)


def checkBST(root: Node | None) -> bool:
    plaint_tree = []
    traverseBST(root, plaint_tree)
    print(plaint_tree)

    result = True
    nodes_count = len(plaint_tree)

    if nodes_count > 1:
        last = plaint_tree[0]
        for i in range(1, nodes_count):
            if plaint_tree[i] <= last:
                return False

            last = plaint_tree[i]

    return result
