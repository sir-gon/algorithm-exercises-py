import unittest
from pathlib import Path

from ....lib.loader import loadTestCases
from .swap_nodes_algo import swapNodes, buildTree, flattenTree

FILE_PATH = str(Path(__file__).resolve().parent)
BIG_TEST_CASES = loadTestCases(FILE_PATH + '/swap_nodes_algo.big.testcases.json')


class TestSwapNodesAlgoBig(unittest.TestCase):
    def test_build_tree_and_flatten_big(self):

        for _, _tt in enumerate(BIG_TEST_CASES):
            t_result: list[int] = flattenTree(buildTree(_tt['nodes']))

            self.assertEqual(
                t_result, _tt['flattened'],
                f"{_} | flattenTree({_tt['nodes']}) must be {_tt['expected']}")

    def test_swap_nodes_big(self):

        for _, _tt in enumerate(BIG_TEST_CASES):

            self.assertEqual(
                swapNodes(_tt['nodes'], _tt['queries']), _tt['expected'],
                f"{_} | swapNodes({_tt['nodes'], _tt['queries']}) must be "
                f"=> {_tt['expected']}")
