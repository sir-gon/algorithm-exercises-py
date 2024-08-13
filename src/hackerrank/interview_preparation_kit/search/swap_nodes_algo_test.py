import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .swap_nodes_algo import swap_nodes, build_tree, plain_tree, swap_branch

FILE_PATH = str(Path(__file__).resolve().parent)
TEST_CASES = load_test_cases(FILE_PATH + '/swap_nodes_algo.testcases.json')


class TestSwapNodesAlgo(unittest.TestCase):

    def test_swap_nodes(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                swap_nodes(_tt['nodes'], _tt['queries']), _tt['answer'],
                f"{_} | swap_nodes({_tt['nodes'], _tt['queries']}) must be "
                f"=> {_tt['answer']}")

    def test_swap_branch(self):

        t_input = None
        t_result = swap_branch(t_input)
        answer = None

        self.assertEqual(
            t_result,
            answer,
            f"swap_branch({t_input}) must be "
            f"=> {answer}"
        )

    def test_build_tree_empty(self):

        t_input = []
        t_to_test = build_tree(t_input)
        t_result = plain_tree(t_to_test)
        answer = [1]

        self.assertEqual(
            t_result,
            answer,
            f"build_tree({t_input}) must be "
            f"=> {answer}"
        )
