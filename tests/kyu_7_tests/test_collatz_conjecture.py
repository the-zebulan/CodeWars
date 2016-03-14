import unittest

from kyu_7.collatz_conjecture import collatz


class CollatzTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(collatz(20), 8)

    def test_equals_2(self):
        self.assertEqual(collatz(15), 18)


if __name__ == '__main__':
    unittest.main()
