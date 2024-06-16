import unittest
from .time_conversion import time_conversion


class TestTimeConversion(unittest.TestCase):

    def test_time_conversion_example(self):

        tests = [
            {'input': '12:01:00PM', 'answer': '12:01:00'},
            {'input': '12:01:00AM', 'answer': '00:01:00'}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                time_conversion(_tt['input']), _tt['answer'],
                f"{_} | time_conversion_({input}) must be "
                f"=> {_tt['answer']}")

    def test_time_conversion_case_0(self):

        tinput = '07:05:45PM'
        solution_found = '19:05:45'

        self.assertEqual(
            time_conversion(tinput), solution_found,
            f"problem0000({input}) must be "
            f"=> {solution_found}")
