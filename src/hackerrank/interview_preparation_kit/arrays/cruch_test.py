import unittest
from .cruch import array_manipulation


class TestCrush(unittest.TestCase):

    def test_array_manipulation(self):

        tests = [
            {
                'title': "Sample Test Case 0",
                'n': 5,
                'queries': [[1, 2, 100],
                            [2, 5, 100],
                            [3, 4, 100]],
                'answer': 200
            },
            {
                'title': "Sample Test Case 1",
                'n': 10,
                'queries': [[1, 5, 3],
                            [4, 8, 7],
                            [6, 9, 1]],
                'answer': 10
            },
            {
                'title': "Sample Test Case 3",
                'n': 10,
                'queries': [[2, 6, 8],
                            [3, 5, 7],
                            [1, 8, 1],
                            [5, 9, 15]],
                'answer': 31
            },
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                array_manipulation(_tt['n'], _tt['queries']), _tt['answer'],
                f"{_} | array_manipulation({_tt['n']}, {_tt['queries']}) must be "
                f"=> {_tt['answer']}")
