import unittest

from katas.kyu_8.subtract_the_sum import SubtractSum


class SubtractSumTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(SubtractSum(191), 'apple')

    def test_equal_2(self):
        self.assertEqual(SubtractSum(946), 'apple')

    def test_equal_3(self):
        self.assertEqual(SubtractSum(315), 'apple')

    def test_equal_4(self):
        self.assertEqual(SubtractSum(656), 'apple')

    def test_equal_5(self):
        self.assertEqual(SubtractSum(826), 'apple')

    def test_equal_6(self):
        self.assertEqual(SubtractSum(806), 'apple')

    def test_equal_7(self):
        self.assertEqual(SubtractSum(623), 'apple')

    def test_equal_8(self):
        self.assertEqual(SubtractSum(807), 'apple')

    def test_equal_9(self):
        self.assertEqual(SubtractSum(719), 'apple')

    def test_equal_10(self):
        self.assertEqual(SubtractSum(111), 'apple')


if __name__ == '__main__':
    unittest.main()
