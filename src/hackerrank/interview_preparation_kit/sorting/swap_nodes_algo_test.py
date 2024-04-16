import unittest
from .swap_nodes_algo import swap_nodes


class TestSwapNodesAlgo(unittest.TestCase):

    tests = [
        {
            'title': 'Sample Test Case 0',
            'nodes': [[2, 3], [-1, -1], [-1, -1]],
            'queries': [1, 1],
            'answer': [[3, 1, 2], [2, 1, 3]]
        },
        {
            'title': 'Sample Test Case 1',
            'nodes': [[2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], [10, 11], [12, 13],
                      [-1, 14], [-1, -1], [15, -1], [16, 17], [-1, -1], [-1, -1],
                      [-1, -1], [-1, -1], [-1, -1], [-1, -1]],
            'queries': [2, 3],
            'answer': [[14, 8, 5, 9, 2, 4, 13, 7, 12, 1, 3, 10, 15, 6, 17, 11, 16],
                       [9, 5, 14, 8, 2, 13, 7, 12, 4, 1, 3, 17, 11, 16, 6, 10, 15]]
        },
        # {
        #     'title': 'Sample 2',
        #     'nodes': [[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9],
        #               [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]],
        #     'queries': [2, 4],
        #     'answer': [[2, 9, 6, 4, 1, 3, 7, 5, 11, 8, 10],
        #                [2, 6, 9, 4, 1, 3, 7, 5, 10, 8, 11]]
        # }
    ]

    def test_swap_nodes(self):

        for _, _tt in enumerate(self.tests):

            self.assertEqual(
                swap_nodes(_tt['nodes'], _tt['queries']), _tt['answer'],
                f"{_} | swap_nodes({_tt['nodes'], _tt['queries']}) must be "
                f"=> {_tt['answer']}")
