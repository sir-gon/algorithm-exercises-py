import unittest
from ...lib.node import Node
from .ctci_is_binary_search_tree import check_bst


class TestIsBinarySearchTree(unittest.TestCase):

    def test_check_bst_test_example(self):
        ref: Node | None = Node(3)
        root: Node | None = ref

        ref.left = Node(2)
        ref.right = Node(5)

        ref = ref.left
        ref.left = Node(1)

        ref = root
        ref = ref.right
        if ref is not None:
            ref.left = Node(6)
            ref.right = Node(1)

        answer = False

        self.assertFalse(
            check_bst(root),
            f"check_bst({root}) must be "
            f"=> {answer}"
        )

    def test_check_bst_test_case_0(self):
        ref: Node | None = Node(3)
        root: Node | None = ref

        ref.left = Node(2)
        ref.right = Node(5)

        ref = ref.left
        ref.left = Node(1)

        ref = root
        ref = ref.right
        if ref is not None:
            ref.left = Node(6)
            ref.right = Node(1)

        answer = False

        self.assertFalse(
            check_bst(root),
            f"check_bst({root}) must be "
            f"=> {answer}"
        )
