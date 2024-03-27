import unittest
from ...lib.tree import BinarySearchTree
from .tree_height_of_a_binary_tree import height

TEST_CASES = [
    {
        'title': 'Test case 0',
        'nodes': [3, 5, 2, 1, 4, 6, 7],
        'answer': 3
    },
    {
        'title': 'Test case 4',
        'nodes': [15],
        'answer': 0
    },
    {
        'title': 'Test case 5',
        'nodes': [3, 1, 7, 5, 4],
        'answer': 3
    }
]


TEST_CASES_BORDER_CASE = [
    {
        'title': 'Test case 0',
        'nodes': [1, 1, 1],
        'answer': 0
    }
]


class TestTreeHeight(unittest.TestCase):

    def test_height(self):

        for _, _tt in enumerate(TEST_CASES):

            tree: BinarySearchTree = BinarySearchTree()

            for x in _tt['nodes']:
                tree.create(x)

            self.assertEqual(
                height(tree.root), _tt['answer'],
                f"{_} | height({tree.root}) must be "
                f"=> {_tt['answer']}")

    def test_height_border_case(self):

        for _, _tt in enumerate(TEST_CASES_BORDER_CASE):

            tree: BinarySearchTree = BinarySearchTree()

            for x in _tt['nodes']:
                tree.create(x)

            self.assertEqual(
                height(tree.root), _tt['answer'],
                f"{_} | height({tree.root}) must be "
                f"=> {_tt['answer']}")
