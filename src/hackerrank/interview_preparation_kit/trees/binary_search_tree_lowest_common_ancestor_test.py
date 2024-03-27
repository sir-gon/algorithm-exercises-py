import unittest
from ...lib.tree import BinarySearchTree
from .binary_search_tree_lowest_common_ancestor import lca, find

TEST_CASES = [
    {
        'title': 'Test case 0',
        'nodes': [4, 2, 3, 1, 7, 6],
        'v1': 1,
        'v2': 7,
        'answer': 4
    },
    {
        'title': 'Test case 4',
        'nodes': [1, 2],
        'v1': 1,
        'v2': 2,
        'answer': 1
    }
]


class TestLastCommonAncestor(unittest.TestCase):

    def test_lca(self):

        for _, _tt in enumerate(TEST_CASES):

            tree: BinarySearchTree = BinarySearchTree(_tt['nodes'])

            self.assertEqual(
                getattr(lca(tree.root, _tt['v1'], _tt['v2']), 'info', None),
                _tt['answer'],
                f"{_} | lca({tree.root}, {_tt['v1']}, {_tt['v2']}) must be "
                f"=> {_tt['answer']}"
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
