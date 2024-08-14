import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from ...lib.tree import BinarySearchTree
from .binary_search_tree_lowest_common_ancestor import lca, find

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(
    FILE_PATH + '/binary_search_tree_lowest_common_ancestor.testcases.json')


class TestLastCommonAncestor(unittest.TestCase):

    def test_lca(self):

        for _, _tt in enumerate(TEST_CASES):

            tree: BinarySearchTree = BinarySearchTree(_tt['nodes'])

            self.assertEqual(
                getattr(lca(tree.root, _tt['v1'], _tt['v2']), 'info', None),
                _tt['expected'],
                f"{_} | lca({tree.root}, {_tt['v1']}, {_tt['v2']}) must be "
                f"=> {_tt['expected']}"
            )

    def test_find(self):

        strange_tree: BinarySearchTree = BinarySearchTree([3, 1, 4])
        non_existing_value = 5
        empty_answer = None

        self.assertIsNone(
            find(strange_tree.root, non_existing_value, []),
            f"find({strange_tree.root}, {non_existing_value}, {[]}) must be "
            f"=> {empty_answer}"
        )

        expected_answer = []

        self.assertEqual(
            find(None, non_existing_value, []),
            expected_answer,
            f"find({strange_tree.root}, {non_existing_value}, {[]}) must be "
            f"=> {[]}"
        )
