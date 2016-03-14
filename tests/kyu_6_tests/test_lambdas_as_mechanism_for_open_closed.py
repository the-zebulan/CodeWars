import unittest

from katas.kyu_6.lambdas_as_mechanism_for_open_closed import (
    greet, shouted, spoken, whispered
)


class LambdasTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(greet(spoken, 'Hello'), 'Hello.')

    def test_equals_2(self):
        self.assertEqual(greet(shouted, 'Hello'), 'HELLO!')

    def test_equals_3(self):
        self.assertEqual(greet(whispered, 'Hello'), 'hello.')


if __name__ == '__main__':
    unittest.main()
