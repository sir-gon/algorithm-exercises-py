from __future__ import annotations
from typing import Any, List, TypeVar

from .binary_node import BinaryNode

T = TypeVar("T")


class BinaryNodeBuilder(BinaryNode[T]):
    def build_binary_node_tree(self, data_tree: Any = None, i: int = 0, j: int = 0):
        if data_tree is None:
            return None

        if i < len(data_tree) and j < len(data_tree[i]):
            result_node = BinaryNode(data_tree[i][j])

            if i + 1 < len(data_tree) and j + 1 < len(data_tree[i + 1]):
                result_node.set_left(
                    self.build_binary_node_tree(data_tree, i + 1, j)
                )

                result_node.set_right(
                    self.build_binary_node_tree(data_tree, i + 1, j + 1)
                )

            return result_node

        return None

    # pylint: disable-next=too-many-arguments, too-many-positional-arguments
    def build_binary_node_tree_weigth(
            self,
            data_tree: Any = None,
            i: int = 0,
            j: int = 0,
            root_value: int = 0,
            leaves_collector: List[int] | None = None
    ):

        if data_tree is None:
            return None

        if i < len(data_tree) and j < len(data_tree[i]):
            current_value = data_tree[i][j] + root_value
            result_node = BinaryNode(data_tree[i][j] + root_value)

            if i + 1 < len(data_tree) and j + 1 < len(data_tree[i + 1]):
                result_node.set_left(
                    self.build_binary_node_tree_weigth(
                        data_tree,
                        i + 1,
                        j,
                        current_value,
                        leaves_collector
                    )
                )

                result_node.set_right(
                    self.build_binary_node_tree_weigth(
                        data_tree,
                        i + 1,
                        j + 1,
                        current_value,
                        leaves_collector
                    )
                )

            if result_node.is_leaf() and leaves_collector is not None:
                leaves_collector.append(current_value)

            return result_node

        return None
