from __future__ import annotations


# pylint: disable=R0903:too-few-public-methods
# Given code:
class Node:
    right: Node | None = None
    left: Node | None = None

    def __init__(self, info):
        self.data = info
        self.left = None
        self.right = None
# End given code
