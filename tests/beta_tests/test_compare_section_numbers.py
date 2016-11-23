import unittest

from katas.beta.compare_section_numbers import compare


class CompareSectionNumbersTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(compare('1', '2'), -1)

    def test_equal_2(self):
        self.assertEqual(compare('1.1', '1.2'), -1)

    def test_equal_3(self):
        self.assertEqual(compare('1.1', '1'), 1)

    def test_equal_4(self):
        self.assertEqual(compare('1.2.3.4', '1.2.3.4'), 0)

    def test_equal_5(self):
        self.assertEqual(compare('3', '3.0'), 0)

    def test_equal_6(self):
        self.assertEqual(compare('3', '3.0.0.0'), 0)

    def test_equal_7(self):
        self.assertEqual(compare('1.2.1', '1.2.0'), 1)

    def test_equal_8(self):
        self.assertEqual(compare('3.0.0', '3.1.1'), -1)

    def test_equal_9(self):
        self.assertEqual(compare('3.0.1', '3.1'), -1)

    def test_equal_10(self):
        self.assertEqual(compare('1.2.3', '1.02.003'), 0)

    def test_equal_11(self):
        self.assertEqual(compare('22.87.95.49.24.8.91.84.80',
                                 '22.87.95.49.24.8.91.84.34.23'), 1)

    def test_equal_12(self):
        self.assertEqual(compare('0.0.0', '1.0.0'), -1)
