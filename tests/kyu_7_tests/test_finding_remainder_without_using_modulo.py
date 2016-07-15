import unittest

from katas.kyu_7.finding_remainder_without_using_modulo import remainder


class RemainderTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(remainder(3, 2), 1)

    def test_equals_2(self):
        self.assertEqual(remainder(19, 2), 1)

    def test_equals_3(self):
        self.assertEqual(remainder(10, 2), 0)

    def test_equals_4(self):
        self.assertEqual(remainder(34, 7), 6)

    def test_equals_5(self):
        self.assertEqual(remainder(27, 5), 2)
