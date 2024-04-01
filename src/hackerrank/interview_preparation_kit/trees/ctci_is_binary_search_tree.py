# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/trees/ctci-is-binary-search-tree.md]] # noqa
# pylint: enable=line-too-long

from ...lib.node import Node


def check_bst(root: Node | None) -> bool:
    if root is None:
        return True

    if root.left is not None and root.left.info > root.info:
        return False

    if root.right is not None and root.right.info < root.info:
        return False

    return check_bst(root.left) and check_bst(root.right)
