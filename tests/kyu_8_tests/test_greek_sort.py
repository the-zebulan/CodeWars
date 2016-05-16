import unittest

from katas.kyu_8.greek_sort import greek_comparator


class GreekComparatorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(greek_comparator('alpha', 'beta'), -1)

    def test_equals_2(self):
        self.assertEqual(greek_comparator('chi', 'chi'), 0)

    def test_equals_3(self):
        self.assertEqual(greek_comparator('upsilon', 'rho'), 1)


if __name__ == '__main__':
    unittest.main()
