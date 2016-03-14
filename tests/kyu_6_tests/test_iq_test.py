import unittest

from katas.kyu_6.iq_test import iq_test


class IQTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(iq_test('2 4 7 8 10'), 3)

    def test_equals_2(self):
        self.assertEqual(iq_test('1 2 1 1'), 2)

    def test_equals_3(self):
        self.assertEqual(iq_test('1 2 2'), 1)


if __name__ == '__main__':
    unittest.main()
