import unittest
from .mark_and_toys import maximum_toys


class TestBubleSort(unittest.TestCase):

    def test_sorts(self):

        tests = [
            {
                'title': 'Sample Test Case 0',
                'budget': 50,
                'prices': [50, 1, 12, 5, 111, 200, 1000, 10],
                'answer': 4
            },
            {
                'title': 'Sample Test Case 1',
                'budget': 7,
                'prices': [1, 2, 3, 4],
                'answer': 3
            },
            {
                'title': 'Sample Test Case 2',
                'budget': 15,
                'prices': [3, 7, 2, 9, 4],
                'answer': 3
            },
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                maximum_toys(_tt['prices'], _tt['budget']), _tt['answer'],
                f"{_} | maximum_toys({_tt['prices'], _tt['budget']}) must be "
                f"=> {_tt['answer']}")
