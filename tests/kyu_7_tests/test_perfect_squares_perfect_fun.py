import unittest

from katas.kyu_7.perfect_squares_perfect_fun import square_it


class SquareItTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(square_it(1), '1')

    def test_equal_2(self):
        self.assertEqual(square_it(222), 'Not a perfect square!')

    def test_equal_3(self):
        self.assertEqual(square_it(234562342342), 'Not a perfect square!')

    def test_equal_4(self):
        self.assertEqual(square_it(88989), 'Not a perfect square!')

    def test_equal_5(self):
        self.assertEqual(square_it(112141568), '112\n141\n568')
