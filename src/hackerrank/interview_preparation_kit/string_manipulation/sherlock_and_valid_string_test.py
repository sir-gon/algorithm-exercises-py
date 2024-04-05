import unittest
from .sherlock_and_valid_string import is_valid

TEST_CASES = [
    {
        'title': 'Sample Test case 0',
        'input': 'aabbccc',
        'answer': True
    },
    {
        'title': 'Sample Test case 0',
        'input': 'aabbcd',
        'answer': False
    },
    {
        'title': 'Sample Test case 1',
        'input': 'aabbccddeefghi',
        'answer': False
    },
    {
        'title': 'Sample Test case 2',
        'input': 'abcdefghhgfedecba',
        'answer': True
    },
    {
        'title': 'Sample Test case 4',
        'input': 'aabbc',
        'answer': True
    }
]


class TestSherklockAndValidString(unittest.TestCase):

    def test_is_valid(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                is_valid(_tt['input']), _tt['answer'],
                f"{_} | is_valid({_tt['input']}) must be "
                f"=> {_tt['answer']}")
