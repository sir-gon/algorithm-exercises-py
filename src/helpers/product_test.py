import unittest

from .product import product

class TestProduct(unittest.TestCase):

    def test_product(self):

        tests = [
          {'input': [], 'answer': 0},
          {'input': ['0', '2', '3', '4'], 'answer': 0},
          {'input': ['1', '2', '3'], 'answer': 6},
          {'input': ['1', '2', '3', '4'], 'answer': 24},
        ]

        for _, _tt in enumerate(tests):
            to_test = product(_tt['input'])

            self.assertEqual( to_test, _tt['answer'],
              f"{_} | product({_tt['input']}) must be "\
                        f"=> {_tt['answer']}")
