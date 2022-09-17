import unittest

from .natural_number import NaturalNumber
class TestDivisors(unittest.TestCase):

    def test_divisors(self):

        tests = [
          {'input': 1, 'answer': [1]},
          {'input': 2, 'answer': [1, 2]},
          {'input': 10, 'answer': [1, 2, 5, 10]},
          {'input': 16, 'answer': [1, 2, 4, 4, 8, 16]}
        ]

        for _, _tt in enumerate(tests):
            to_test = NaturalNumber(_tt['input'])

            self.assertEqual( to_test.divisors(), _tt['answer'],
              f"{_} | NaturalNumber({_tt['input']}).divisors() must be => {_tt['answer']}")

    def test_unique_divisors(self):

        tests = [
          {'input': 1, 'answer': [1]},
          {'input': 2, 'answer': [1, 2]},
          {'input': 9, 'answer': [1, 3, 9]},
          {'input': 16, 'answer': [1, 2, 4, 8, 16]}
        ]

        for _, _tt in enumerate(tests):
            to_test = NaturalNumber(_tt['input'])

            self.assertEqual( to_test.divisors_unique(), _tt['answer'],
              f"{_} | NaturalNumber({_tt['input']}).divisors() must be => {_tt['answer']}")

    def test_prime_factor(self):
        tests = [
          {'input': 1, 'answer': 1, 'divisor': 1, 'cycles': 0},
          {'input': 2, 'answer': 2, 'divisor': 1, 'cycles': 1},
          {'input': 4, 'answer': 2, 'divisor': 2, 'cycles': 1},
          {'input': 9, 'answer': 3, 'divisor': 3, 'cycles': 2},
          {'input': 7, 'answer': 7, 'divisor': 1, 'cycles': 6},
        ]

        for _, _tt in enumerate(tests):
            to_test = NaturalNumber(_tt['input'])

            message =  f"{_} | NaturalNumber({_tt['input']}).get_prime_factor() must be => {_tt['answer']}"
            self.assertEqual( to_test.get_prime_factor(), _tt['answer'], message)

            message = f"{_} | NaturalNumber({_tt['input']}).get_divisor() must be => {_tt['divisor']}"
            self.assertEqual( to_test.get_divisor(), _tt['divisor'], message)

            message = f"{_} | NaturalNumber({_tt['input']}).get_prime_factor() must be => {_tt['cycles']}"
            self.assertEqual(to_test.get_prime_factor_cycles(), _tt['cycles'], message)

    def test_prime(self):
        tests = [
          {'input': 2, 'answer': True},
          {'input': 5, 'answer': True},
          {'input': 7, 'answer': True}
        ]

        for _, _tt in enumerate(tests):
            to_test = NaturalNumber(_tt['input'])

            message = f"{_} | NaturalNumber({_tt['input']}).is_prime() must be => {_tt['answer']}"
            self.assertEqual( to_test.is_prime(), _tt['answer'], message)


    def test_not_prime(self):
        tests = [
          {'input': 1, 'answer': False},
          {'input': 10, 'answer': False},
          {'input': 16, 'answer': False}
        ]

        for _, _tt in enumerate(tests):
            to_test = NaturalNumber(_tt['input'])

            message = f"{_} | NaturalNumber({_tt['input']}).is_prime() must be => {_tt['answer']}"
            self.assertEqual( to_test.is_prime(), _tt['answer'], message)

    def test_prime_factors(self):
        tests = [
          {'input': 1, 'answer': [1], 'cycles': 1},
          {'input': 2, 'answer': [2], 'cycles': 1},
          {'input': 6, 'answer': [2, 3], 'cycles': 3}
        ]

        for _, _tt in enumerate(tests):
            to_test = NaturalNumber(_tt['input'])

            message = f"{_} | NaturalNumber({_tt['input']}).prime_factors() must be => {_tt['answer']}"
            self.assertEqual( to_test.prime_factors(), _tt['answer'], message)
