import unittest
from .swap_nodes_algo import swap_nodes, build_tree, plain_tree, swap_branch


class TestSwapNodesAlgo(unittest.TestCase):

    tests = [
        {
            'title': 'Sample 0',
            'nodes': [[2, 3], [-1, -1], [-1, -1]],
            'queries': [1, 1],
            'answer': [[3, 1, 2], [2, 1, 3]]
        },
        {
            'title': 'Sample 1',
            'nodes': [[2, 3], [-1, 4], [-1, 5], [-1, -1], [-1, -1]],
            'queries': [2],
            'answer': [[4, 2, 1, 5, 3]]
        },
        {
            'title': 'Sample 2',
            'nodes': [[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9],
                      [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]],
            'queries': [2, 4],
            'answer': [[2, 9, 6, 4, 1, 3, 7, 5, 11, 8, 10],
                       [2, 6, 9, 4, 1, 3, 7, 5, 10, 8, 11]]
        },
        {
            'title': 'Sample Test Case 1',
            'nodes': [[2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], [10, 11], [12, 13],
                      [-1, 14], [-1, -1], [15, -1], [16, 17], [-1, -1], [-1, -1],
                      [-1, -1], [-1, -1], [-1, -1], [-1, -1]],
            'queries': [2, 3],
            'answer': [[14, 8, 5, 9, 2, 4, 13, 7, 12, 1, 3, 10, 15, 6, 17, 11, 16],
                       [9, 5, 14, 8, 2, 13, 7, 12, 4, 1, 3, 17, 11, 16, 6, 10, 15]]
        }
    ]

    def test_swap_nodes(self):

        for _, _tt in enumerate(self.tests):

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
