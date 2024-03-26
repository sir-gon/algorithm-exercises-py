# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/trees/tree-height-of-a-binary-tree.md]] # noqa
# pylint: enable=line-too-long

from __future__ import annotations


# pylint: disable=R0903:too-few-public-methods
# Given code:
class Node:
    left: Node | None = None
    right: Node | None = None

    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
            return

        current = self.root

        while True:
            if val < current.info:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(val)
                    break
            elif val > current.info:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(val)
                    break
            else:
                break
# End given code


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
