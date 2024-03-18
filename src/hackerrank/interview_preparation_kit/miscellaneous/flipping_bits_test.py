import unittest
from .flipping_bits import flipping_bits

TEST_CASES = [
    {
        'title': 'Sample Test Case 0',
        'tests':
        [
            {
                'input': 2147483647,
                'answer': 2147483648
            },
            {
                'input': 1,
                'answer': 4294967294
            },
            {
                'input': 0,
                'answer': 4294967295
            }
        ]
    },
    {
        'title': 'Sample Test Case 1',
        'tests':
        [

            {
                'input': 4,
                'answer': 4294967291
            },
            {
                'input': 123456,
                'answer': 4294843839
            }
        ]
    },
    {
        'title': 'Sample Test Case 2',
        'tests':
        [

            {
                'input': 0,
                'answer': 4294967295
            },
            {
                'input': 802743475,
                'answer': 3492223820
            },
            {
                'input': 35601423,
                'answer': 4259365872
            }
        ]
    }
]


class TestFlippingBits(unittest.TestCase):

    def test_flipping_bits(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    flipping_bits(_tt['input']), _tt['answer'],
                    f"{_} | flipping_bits({_tt['input']}) must be "
                    f"=> {_tt['answer']}")
