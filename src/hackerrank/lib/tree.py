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
    def __init__(self, nodes: list[int] | None = None):
        self.root = None
        if nodes is not None:
            for x in nodes:
                self.create(x)

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
