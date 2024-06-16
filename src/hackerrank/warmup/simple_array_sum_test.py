import unittest
from .simple_array_sum import simple_array_sum


class TestSimpleArraySum(unittest.TestCase):

    def test_simple_array_sum(self):

        tests = [
            {'input': [1, 2, 3, 4, 10, 11], 'answer': 31}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                simple_array_sum(_tt['input']), _tt['answer'],
                f"{_} | simple_array_sum({_tt['input']}) must be "
                f"=> {_tt['answer']}")
