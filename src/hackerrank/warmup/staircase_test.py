import unittest
from .staircase import staircase


class TestStaircase(unittest.TestCase):

    def test_staircase(self):

        tests = [
          {
            'input': 6,
            'answer': '\n'.join([
                '     #',
                '    ##',
                '   ###',
                '  ####',
                ' #####',
                '######'
                ])
          }
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                staircase(_tt['input']), _tt['answer'],
                f"{_} | staircase({_tt['input']}) must be "
                f"=> {_tt['answer']}")
