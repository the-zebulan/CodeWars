import unittest

from katas.kyu_7.split_the_bill import split_the_bill


class SplitTheBillTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(split_the_bill({'A': 20, 'B': 15, 'C': 10}),
                         {'A': 5, 'B': 0, 'C': -5})

    def test_equals_2(self):
        self.assertEqual(split_the_bill({'A': 40, 'B': 25, 'X': 10}),
                         {'A': 15, 'B': 0, 'X': -15})


if __name__ == '__main__':
    unittest.main()
