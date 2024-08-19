import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from ....hackerrank.lib.node import Node
from .swap_nodes_algo import swap_nodes, build_tree, flatten_tree, swap_branch

FILE_PATH = str(Path(__file__).resolve().parent)
TEST_CASES = load_test_cases(FILE_PATH + '/swap_nodes_algo.testcases.json')


class TestSwapNodesAlgo(unittest.TestCase):
    def test_swap_nodes(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                swap_nodes(_tt['nodes'], _tt['queries']), _tt['expected'],
                f"{_} | swap_nodes({_tt['nodes'], _tt['queries']}) must be "
                f"=> {_tt['expected']}")

    def test_swap_branch(self):

        t_input = None
        t_result = swap_branch(t_input)
        expected = None

        self.assertEqual(
            t_result,
            expected,
            f"swap_branch({t_input}) must be "
            f"=> {expected}"
        )

    def test_build_tree_and_plain(self):

        for _, _tt in enumerate(TEST_CASES):

            t_to_test: Node = build_tree(_tt['nodes'])
            t_result: list[int] = flatten_tree(t_to_test)

            self.assertEqual(
                t_result, _tt['flattened'],
                f"{_} | flatten_tree({_tt['nodes']}) must be {_tt['expected']}")

    def test_build_tree_empty(self):

        t_input = []
        t_to_test = build_tree(t_input)
        t_result = flatten_tree(t_to_test)
        expected = [1]

        self.assertEqual(
            t_result,
            expected,
            f"build_tree({t_input}) must be "
            f"=> {expected}"
        )
