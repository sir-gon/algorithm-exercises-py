import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from ...lib.tree import BinarySearchTree
from .tree_height_of_a_binary_tree import height

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(
    FILE_PATH + '/tree_height_of_a_binary_tree.testcases.json')


TEST_CASES_BORDER_CASE = [
    {
        'title': 'Test case 0',
        'nodes': [1, 1, 1],
        'expected': 0
    }
]


class TestTreeHeight(unittest.TestCase):

    def test_height(self):

        for _, _tt in enumerate(TEST_CASES):

            tree: BinarySearchTree = BinarySearchTree()

            for nodes in _tt['nodes']:
                tree.create(nodes)

            self.assertEqual(
                height(tree.root), _tt['expected'],
                f"{_} | height({tree.root}) must be "
                f"=> {_tt['expected']}")

    def test_height_border_case(self):

        for _, _tt in enumerate(TEST_CASES_BORDER_CASE):

            tree: BinarySearchTree = BinarySearchTree()

            for nodes in _tt['nodes']:
                tree.create(nodes)

            self.assertEqual(
                height(tree.root), _tt['expected'],
                f"{_} | height({tree.root}) must be "
                f"=> {_tt['expected']}")
