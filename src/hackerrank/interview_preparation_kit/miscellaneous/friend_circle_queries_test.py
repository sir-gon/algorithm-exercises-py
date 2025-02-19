import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .friend_circle_queries import maxCircle


FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(
    FILE_PATH + '/friend_circle_queries.testcases.json')


class TestFriendCircle(unittest.TestCase):

    def test_max_circle(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                maxCircle(_tt['arr']), _tt['answer'],
                f"{_} | maxCircle({_tt['arr']}) must be "
                f"=> {_tt['answer']} in {_tt['title']}")
