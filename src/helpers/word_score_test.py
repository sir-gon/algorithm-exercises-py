import unittest

from .word_score import word_score


class TestWordScore(unittest.TestCase):

    def test_wordscore(self):

        tests = [
          {'input': 'ABC', 'answer': 1 + 2 + 3},
          {'input': 'OTTO', 'answer': 15 * 2 + 20 * 2},
          {'input': 'COLIN', 'answer': 53},
        ]

        for _, _tt in enumerate(tests):
            to_test = word_score(_tt['input'])

            self.assertEqual(
                to_test, _tt['answer'],
                f"{_} | word_score({_tt['input']}) must be "
                f"=> {_tt['answer']}")

    def test_wordscore_with_scoreless_characters(self):

        tests = [
          {'input': '-A B C-', 'answer': 1 + 2 + 3},
          {'input': 'O.T.T.O', 'answer': 15 * 2 + 20 * 2},
        ]

        for _, _tt in enumerate(tests):
            to_test = word_score(_tt['input'])

            self.assertEqual(
                to_test, _tt['answer'],
                f"{_} | word_score({_tt['input']}) must be "
                f"=> {_tt['answer']}")
