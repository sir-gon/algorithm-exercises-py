import unittest

from .binary_node import BinaryNode
from .binary_node_builder import BinaryNodeBuilder

data = [[75], [95, 64]]


class TestBinaryNodeBuilder(unittest.TestCase):
    def test_builder_none(self):
        value = None

        builder = BinaryNodeBuilder[int]()
        tree = builder.build_binary_node_tree()

        self.assertIsNotNone(builder, f"BinaryNodeBuilder() must be => !{None}")

        self.assertIsNone(tree, f"BinaryNodeBuilder({value}) must be => {None}")

    def test_builder_with_values(self):
        tree = BinaryNodeBuilder[int]().build_binary_node_tree(data, 0, 0)
        compared_tree = BinaryNode(75, BinaryNode(95), BinaryNode(64))

        self.assertEqual(tree, compared_tree)

    def test_builder_with_invalid_coordinates(self):
        self.assertIsNone(BinaryNodeBuilder[int]().build_binary_node_tree(data, 0, 5))
        self.assertIsNone(BinaryNodeBuilder[int]().build_binary_node_tree(data, 5, 0))

    def test_builder_with_weights_none(self):
        value = None

        builder = BinaryNodeBuilder[int]()
        tree = builder.build_binary_node_tree_weigth()

        self.assertIsNotNone(builder, f"BinaryNodeBuilder() must be => !{None}")

        self.assertIsNone(tree, f"BinaryNodeBuilder({value}) must be => {None}")

    def test_builder_with_weights_with_values(self):
        tree = BinaryNodeBuilder[int]().build_binary_node_tree_weigth(data, 0, 0)
        compared_tree = BinaryNode(75, BinaryNode(170), BinaryNode(139))

        self.assertEqual(tree, compared_tree)

    def test_builder_with_weights_with_invalid_coordinates(self):
        self.assertIsNone(
            BinaryNodeBuilder[int]().build_binary_node_tree_weigth(data, 0, 5)
        )
        self.assertIsNone(
            BinaryNodeBuilder[int]().build_binary_node_tree_weigth(data, 5, 0)
        )

    def test_builder_with_weights_with_values_leaves(self):
        leaves = []
        tree = BinaryNodeBuilder[int]().build_binary_node_tree_weigth(
            data, 0, 0, 0, leaves
        )

        compared_leaves = [170, 139]

        self.assertIsNotNone(tree)
        self.assertEqual(leaves, compared_leaves)
