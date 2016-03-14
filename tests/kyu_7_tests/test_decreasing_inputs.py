import unittest

from kyu_7.decreasing_inputs import add


class DescreasingInputsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(add(100, 200, 300), 300)

    def test_equals_2(self):
        self.assertEqual(add(2), 2)

    def test_equals_3(self):
        self.assertEqual(add(4, -3, -2), 2)


if __name__ == '__main__':
    unittest.main()
