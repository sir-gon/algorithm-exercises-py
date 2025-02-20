import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .swap_nodes_algo import swapNodes, swapBranch, buildTree, flattenTree

FILE_PATH = str(Path(__file__).resolve().parent)
TEST_CASES = loadTestCases(FILE_PATH + '/swap_nodes_algo.testcases.json')


class TestSwapNodesAlgo(unittest.TestCase):
    def test_swap_nodes(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                swapNodes(_tt['nodes'], _tt['queries']), _tt['expected'],
                f"{_} | swapNodes({_tt['nodes'], _tt['queries']}) must be "
                f"=> {_tt['expected']}")

    def test_swap_branch(self):

        t_input = None
        t_result = swapBranch(t_input)
        expected = None

        self.assertEqual(
            t_result,
            expected,
            f"swapBranch({t_input}) must be "
            f"=> {expected}"
        )

    def test_build_tree_and_plain(self):

        for _, _tt in enumerate(TEST_CASES):

            t_result: list[int] = flattenTree(buildTree(_tt['nodes']))

            self.assertEqual(
                t_result, _tt['flattened'],
                f"{_} | flattenTree({_tt['nodes']}) must be {_tt['expected']}")

    def test_build_tree_empty(self):

        t_input = []
        t_to_test = buildTree(t_input)
        t_result = flattenTree(t_to_test)
        expected = [1]

        self.assertEqual(
            t_result,
            expected,
            f"buildTree({t_input}) must be "
            f"=> {expected}"
        )
