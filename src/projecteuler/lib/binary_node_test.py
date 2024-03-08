import unittest

from .binary_node import BinaryNode


class TestBinaryNode(unittest.TestCase):

    def test_get_value_none(self):

        value = None

        test_node_a = BinaryNode[int]()

        self.assertEqual(
            test_node_a.get_value(), value,
            f"BinaryNode({value}).get_value() must be => {value}")

    def test_get_value(self):

        value = 5

        test_node_a = BinaryNode[int](5)
        test_node_b = BinaryNode[int](test_node_a)
        test_node_c = BinaryNode[int]()
        test_node_c.set_value(value)
        test_node_d = BinaryNode[int](test_node_c)

        self.assertEqual(
            test_node_a.get_value(), value,
            f"BinaryNode({value}).get_value() must be => {value}")

        self.assertEqual(
            test_node_b.get_value(), value,
            f"BinaryNode({value}).get_value() must be => {value}")

        self.assertEqual(
            test_node_c.get_value(), value,
            f"BinaryNode({value}).get_value() must be => {value}")

        self.assertEqual(
            test_node_d.get_value(), value,
            f"BinaryNode({value}).get_value() must be => {value}")

    def test_binary_node_left_value(self):
        value_a = 'A'
        value_left = 'Z'

        test_node_a = BinaryNode[str](value_a)
        test_node_a.set_left(value_left)

        self.assertIsNotNone(
            test_node_a.get_left(),
            f"BinaryNode({value_a}).value_left({value_left}) must have a value")

        self.assertEqual(
            test_node_a.left and test_node_a.left.get_value(), value_left,
            f"BinaryNode({value_a}).value_left({value_left}) must be => {value_left}")

    def test_binary_node_right_value(self):
        value_a = 'A'
        value_right = 'Z'

        test_node_a = BinaryNode[str](value_a)
        test_node_a.set_right(value_right)

        self.assertIsNotNone(
            test_node_a.get_right(),
            f"BinaryNode({value_a}).value_right({value_right}) must have a value")

        self.assertEqual(
            test_node_a.right and test_node_a.right.get_value(), value_right,
            f"BinaryNode({value_a}).value_right({value_right}) must be => {value_right}")

    def test_binary_node_leaf_condition(self):
        value_a = 'A'

        test_node_a = BinaryNode[str](value_a)
        test_node_b = BinaryNode[str]('B')
        test_node_c = BinaryNode[str]('C')

        test_node_a.set_left(test_node_b)
        test_node_a.set_right(test_node_c)

        self.assertFalse(
            test_node_a.is_leaf(),
            f"BinaryNode({value_a}).is_leaf() must be => {False}")

        self.assertTrue(
            test_node_b.is_leaf(),
            f"BinaryNode({'B'}).is_leaf() must be => {True}")

        self.assertTrue(
            test_node_c.is_leaf(),
            f"BinaryNode({'C'}).is_leaf() must be => {True}")

    def test_binary_node_equality(self):

        test_node_none_a = BinaryNode[str]()
        test_node_none_b = BinaryNode[str]()

        self.assertEqual(test_node_none_a, test_node_none_b)

        test_node_a = BinaryNode[str]('A')
        test_node_b = BinaryNode[str]('A')

        self.assertEqual(test_node_a, test_node_b)

        test_node_x = BinaryNode[str]('A')
        test_node_x.set_left('B')
        test_node_x.set_right('C')

        test_node_y = BinaryNode[str]('A', 'B', 'C')

        self.assertEqual(test_node_x, test_node_y)

        test_node_q = BinaryNode[str]('A', None, 'C')
        test_node_p = BinaryNode[str]('A', 'B', None)

        self.assertNotEqual(test_node_q, test_node_p)
