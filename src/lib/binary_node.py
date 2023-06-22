from __future__ import annotations
from typing import Generic, TypeVar

T = TypeVar("T")


class BinaryNode(Generic[T]):
    def __init__(
        self,
        value: T | BinaryNode | None = None,
        left: T | BinaryNode | None = None,
        right: T | BinaryNode | None = None,
    ):
        self.value = None
        self.left = None
        self.right = None

        self.set_value(value)
        self.set_left(left)
        self.set_right(right)

    def __eq__(self, other) -> bool:
        if isinstance(self, other.__class__):
            return (
                self.value == other.value
                and self.left == other.left
                and self.right == other.right
            )

        return False

    def set_value(self, value: T | BinaryNode | None) -> BinaryNode | None:
        if isinstance(value, BinaryNode):
            self.value = value.get_value()
        else:
            self.value = value

        return self

    def get_value(self) -> T | None:
        return self.value

    def set_left(self, left: T | BinaryNode | None) -> BinaryNode | None:
        if left is None:
            self.left = None
            return self

        if isinstance(left, BinaryNode):
            self.left = left
        else:
            self.left = BinaryNode(left)

        return self

    def get_left(self) -> T | BinaryNode | None:
        return self.left

    def set_right(self, right: T | BinaryNode | None) -> BinaryNode | None:
        if right is None:
            self.right = None
            return self

        if isinstance(right, BinaryNode):
            self.right = right
        else:
            self.right = BinaryNode(right)

        return self

    def get_right(self) -> T | BinaryNode | None:
        return self.right

    def is_leaf(self) -> bool:
        return self.get_left() is None and self.get_right() is None
