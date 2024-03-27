# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/trees/tree-height-of-a-binary-tree.md]] # noqa
# pylint: enable=line-too-long

from ...lib.tree import Node


def height(root: Node | None):
    result: int = 0

    if root is None:
        return 0

    if root.left is not None or root.right is not None:
        return 1 + max(
            height(root.left),
            height(root.right)
        )

    return result
