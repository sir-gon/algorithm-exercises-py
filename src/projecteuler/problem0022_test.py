import unittest
import json
import os
from .problem0022 import problem0022


class TestProblem0022(unittest.TestCase):

    def test_problem0022(self):
        file_abs_path = os.path.abspath(os.path.dirname(__file__))

        with open(
                os.path.join(file_abs_path, 'data', 'p022_names.json'),
                encoding="utf-8") as read_content:

            names = json.load(read_content)
            solution_found = 871198282

            self.assertEqual(
                problem0022(names), solution_found,
                f"problem0022({names}) must be "
                f"=> {solution_found}")
