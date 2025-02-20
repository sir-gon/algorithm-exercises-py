import unittest
from ...lib.node import Node
from .ctci_is_binary_search_tree import checkBST


class TestIsBinarySearchTree(unittest.TestCase):

    def test_check_bst_edge_case(self):
        root: Node | None = None

        answer = True

        self.assertTrue(
            checkBST(root),
            f"checkBST({root}) must be "
            f"=> {answer}"
        )

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
            checkBST(root),
            f"checkBST({root}) must be "
            f"=> {answer}"
        )

    def test_check_bst_test_case_0(self):
        ref: Node | None = Node(4)
        root: Node | None = ref

        ref.left = Node(2)
        ref.right = Node(6)

        ref = ref.left
        ref.left = Node(1)
        ref.right = Node(3)

        ref = root
        ref = ref.right
        if ref is not None:
            ref.left = Node(5)
            ref.right = Node(7)

        answer = True

        self.assertTrue(
            checkBST(root),
            f"checkBST({root}) must be "
            f"=> {answer}"
        )

    def test_check_bst_test_case_1(self):
        ref: Node | None = Node(3)
        root: Node | None = ref

        ref.left = Node(2)
        ref.right = Node(6)

        ref = ref.left
        ref.left = Node(1)
        ref.right = Node(4)

        ref = root
        ref = ref.right
        if ref is not None:
            ref.left = Node(5)
            ref.right = Node(7)

        answer = False

        self.assertFalse(
            checkBST(root),
            f"checkBST({root}) must be "
            f"=> {answer}"
        )

    def test_check_bst_test_case_2(self):
        ref: Node | None = Node(9)
        root: Node | None = ref

        ref.left = Node(5)
        ref.right = Node(13)

        ref = ref.left
        ref.left = Node(3)
        ref.right = Node(7)

        ref = root
        ref = ref.right
        if ref is not None:
            ref.left = Node(11)
            ref.right = Node(15)

        answer = True

        self.assertTrue(
            checkBST(root),
            f"checkBST({root}) must be "
            f"=> {answer}"
        )
