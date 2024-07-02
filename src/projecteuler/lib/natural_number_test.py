import unittest

from .natural_number import (
    NaturalNumber
)


class TestDivisors(unittest.TestCase):

    def test_value(self):

        tests = [
            {'input': 1, 'answer': 1},
            {'input': 2, 'answer': 2},
            {'input': 10, 'answer': 10},
            {'input': 16, 'answer': 16}
        ]

        for _, _tt in enumerate(tests):
            to_test = NaturalNumber(_tt['input'])

            self.assertEqual(
                to_test.get_value(), _tt['answer'],
                f"{_} | NaturalNumber({_tt['input']}).get_value() must be "
                f"=> {_tt['answer']}")

    def test_divisors_of_one(self):

        tests = [
            {'input': 1, 'answer': [1], 'cycles': 0},
        ]

        for _, _tt in enumerate(tests):
            to_test = NaturalNumber(_tt['input'])

            self.assertEqual(
                to_test.divisors(), _tt['answer'],
                f"{_} | NaturalNumber({_tt['input']}).divisors() must be "
                f"=> {_tt['answer']}")

            self.assertEqual(
                to_test.get_divisors_cycles(), _tt['cycles'],
                f"{_} | NaturalNumber({_tt['input']}).get_divisors_cycles() "
                f"must be => {_tt['cycles']}")

    def test_divisors(self):

        test_cases = [
            {'input': 2, 'answer': [1, 2], 'cycles': 1},
            {'input': 8, 'answer': [1, 2, 4, 8], 'cycles': 2},
            {'input': 10, 'answer': [1, 2, 5, 10], 'cycles': 2},
            {'input': 16, 'answer': [1, 2, 4, 8, 16], 'cycles': 3}
        ]

        edge_stest_cases = [
            {'input': 110, 'answer': [1, 2, 5, 10, 11, 22, 55, 110], 'cycles': 10},
            {'input': 18632, 'answer': [
                1, 2, 4, 8, 17, 34, 68, 136, 137,
                274, 548, 1096, 2329, 4658, 9316, 18632],
             'cycles': 136}
        ]

        test_cases = test_cases + edge_stest_cases

        for _, _tt in enumerate(test_cases):
            to_test = NaturalNumber(_tt['input'])

            self.assertEqual(
                to_test.divisors(), _tt['answer'],
                f"{_} | NaturalNumber({_tt['input']}).divisors() must be "
                f"=> {_tt['answer']}")

            self.assertEqual(
                to_test.get_divisors_cycles(), _tt['cycles'],
                f"{_} | NaturalNumber({_tt['input']}).get_divisors_cycles() "
                f"must be => {_tt['cycles']}")

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

            message = f"{_} | NaturalNumber({_tt['input']}).get_prime_factor() "\
                      f"must be => {_tt['answer']}"
            self.assertEqual(to_test.get_prime_factor(), _tt['answer'], message)

            message = f"{_} | NaturalNumber({_tt['input']}).get_divisor() "\
                      f"must be => {_tt['divisor']}"
            self.assertEqual(to_test.get_divisor(), _tt['divisor'], message)

            message = f"{_} | NaturalNumber({_tt['input']}).get_prime_factor_cycles() "\
                      f"must be => {_tt['cycles']}"
            self.assertEqual(to_test.get_prime_factor_cycles(), _tt['cycles'], message)

    def test_prime_factor_without_cache(self):
        tests = [
            {'input': 1, 'answer': 1, 'divisor': 1, 'cycles': 0},
            {'input': 2, 'answer': 2, 'divisor': 1, 'cycles': 1},
            {'input': 4, 'answer': 2, 'divisor': 2, 'cycles': 1},
            {'input': 9, 'answer': 3, 'divisor': 3, 'cycles': 2},
            {'input': 7, 'answer': 7, 'divisor': 1, 'cycles': 6},
        ]

        for _, _tt in enumerate(tests):
            to_test = NaturalNumber(_tt['input'])

            message = f"{_} | NaturalNumber({_tt['input']}).get_divisor() "\
                      f"must be => {_tt['divisor']}"
            self.assertEqual(to_test.get_divisor(), _tt['divisor'], message)

    def test_prime_factor_cycles_without_cache(self):
        tests = [
            {'input': 1, 'answer': 1, 'divisor': 1, 'cycles': 0},
            {'input': 2, 'answer': 2, 'divisor': 1, 'cycles': 1},
            {'input': 4, 'answer': 2, 'divisor': 2, 'cycles': 1},
            {'input': 9, 'answer': 3, 'divisor': 3, 'cycles': 2},
            {'input': 7, 'answer': 7, 'divisor': 1, 'cycles': 6},
        ]

        for _, _tt in enumerate(tests):
            to_test = NaturalNumber(_tt['input'])

            message = f"{_} | NaturalNumber({_tt['input']}).get_prime_factor_cycles() "\
                      f"must be => {_tt['cycles']}"
            self.assertEqual(to_test.get_prime_factor_cycles(), _tt['cycles'], message)

    def test_prime_and_cache(self):
        tests = [
            {'input': 2, 'answer': True, 'cycles': 1},
            {'input': 5, 'answer': True, 'cycles': 4},
            {'input': 7, 'answer': True, 'cycles': 6}
        ]

        for _, _tt in enumerate(tests):
            to_test = NaturalNumber(_tt['input'])

            message = f"{_} | NaturalNumber({_tt['input']}).is_prime()"\
                      f" first time must be => {_tt['answer']}"
            self.assertEqual(to_test.is_prime(), _tt['answer'], message)

            message = f"{_} | NaturalNumber({_tt['input']}).is_prime()"\
                      f" with cache must be => {_tt['answer']}"
            self.assertEqual(to_test.is_prime(), _tt['answer'], message)

            message = f"{_} | NaturalNumber({_tt['input']}).get_prime_cycles() must be "\
                      f"=> {_tt['cycles']}"
            self.assertEqual(to_test.get_prime_cycles(), _tt['cycles'], message)

    def test_not_prime(self):
        tests = [
            {'input': 1, 'answer': False},
            {'input': 10, 'answer': False},
            {'input': 16, 'answer': False}
        ]

        for _, _tt in enumerate(tests):
            to_test = NaturalNumber(_tt['input'])

            message = f"{_} | NaturalNumber({_tt['input']}).is_prime() must be "\
                      f"=> {_tt['answer']}"
            self.assertEqual(to_test.is_prime(), _tt['answer'], message)

    def test_prime_factors_and_cache(self):
        tests = [
            {'input': 1, 'answer': [1], 'cycles': 0},
            {'input': 2, 'answer': [2], 'cycles': 1},
            {'input': 6, 'answer': [2, 3], 'cycles': 3},
            {'input': 12, 'answer': [2, 2, 3], 'cycles': 4}
        ]

        for _, _tt in enumerate(tests):
            to_test = NaturalNumber(_tt['input'])

            message = f"{_} | NaturalNumber({_tt['input']}).prime_factors()"\
                      f" fisrt time must be => {_tt['answer']}"
            self.assertEqual(to_test.prime_factors(), _tt['answer'], message)

            message = f"{_} | NaturalNumber({_tt['input']}).prime_factors()"\
                      f" with cache must be => {_tt['answer']}"
            self.assertEqual(to_test.prime_factors(), _tt['answer'], message)

            message = f"{_} | NaturalNumber({_tt['input']}).get_prime_factors_cycles()"\
                      f" must be => {_tt['cycles']}"
            self.assertEqual(to_test.get_prime_factors_cycles(), _tt['cycles'], message)
