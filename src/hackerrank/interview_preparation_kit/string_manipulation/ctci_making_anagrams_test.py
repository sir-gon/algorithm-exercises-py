import unittest
from .ctci_making_anagrams import make_anagram

TEST_CASES = [
    {
        'title': 'Sample Test case 0',
        'a': 'cde',
        'b': 'abc',
        'answer': 4
    },
    {
        'title': 'Sample Test case 1',
        'a': 'fcrxzwscanmligyxyvym',
        'b': 'jxwtrhvujlmrpdoqbisbwhmgpmeoke',
        'answer': 30
    },
    {
        'title': 'Sample Test case 2',
        'a': 'showman',
        'b': 'woman',
        'answer': 2
    }
]


class TestMakeAnagram(unittest.TestCase):

    def test_make_anagram(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                make_anagram(_tt['a'], _tt['b']), _tt['answer'],
                f"{_} | make_anagram({_tt['a']}, {_tt['b']}) must be "
                f"=> {_tt['answer']}")
