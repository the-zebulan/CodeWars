import unittest

from katas.kyu_5.excels_countif_sumif_averageif_functions import \
    average_if, count_if, sum_if


class ExcelFunctionsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(count_if([1, 3, 5, 3], 3), 2)

    def test_equals_2(self):
        self.assertEqual(count_if(
            ['John', 'Steve', 'Rachel', 'Rebecca', 'John', 'John'], 'John'
            ), 3
        )

    def test_equals_3(self):
        self.assertEqual(count_if([1, 3, 5, 3], '>=3'), 3)

    def test_equals_4(self):
        self.assertEqual(count_if([1.5, 3, 5, 3, 0, -1, -5], '<=1.5'), 4)

    def test_equals_5(self):
        self.assertEqual(count_if([1, 3, 5, 3.5], '>3'), 2)

    def test_equals_6(self):
        self.assertEqual(count_if([1, 3, 5, 3, 0, -1, -5], '<1'), 3)

    def test_equals_7(self):
        self.assertEqual(count_if([1, 3, 5, 3, 0, -1, -5], '<>1'), 6)

    def test_equals_8(self):
        self.assertEqual(count_if([1, 3, 5, 7, 9], 3), 1)

    def test_equals_9(self):
        self.assertEqual(count_if(['John', 'Steve', 'John'], 'John'), 2)

    def test_equals_10(self):
        self.assertEqual(sum_if([2, 4, 6, -1, 3, 1.5], '>0'), 16.5)

    def test_equals_11(self):
        self.assertEqual(sum_if([1, 3, 5, 3], 3), 6)

    def test_equals_12(self):
        self.assertEqual(sum_if([1, 3, 5, 3], '>=3'), 11)

    def test_equals_13(self):
        self.assertEqual(sum_if([1.5, 3, 5, 3, 0, -1, -5], '<=1.5'), -4.5)

    def test_equals_14(self):
        self.assertEqual(sum_if([1, 3, 5, 3.5], '>3'), 8.5)

    def test_equals_15(self):
        self.assertEqual(sum_if([1, 3, 5, 3, 0, -1, -5], '<1'), -6)

    def test_equals_16(self):
        self.assertEqual(sum_if([1, 3, 5, 3, 0, -1, -5], '<>1'), 5)

    def test_equals_17(self):
        self.assertEqual(average_if([1, 3, 5, 3], 3), 3)

    def test_equals_18(self):
        self.assertEqual(average_if([1, 3, 5, 3], '>=3'), 11 / 3.0)

    def test_equals_19(self):
        self.assertEqual(average_if(
            [1.5, 3, 5, 3, 0, -1, -5], '<=1.5'), -1.125
        )

    def test_equals_20(self):
        self.assertEqual(average_if([1, 3, 5, 3.5], '>3'), 4.25)

    def test_equals_21(self):
        self.assertEqual(average_if([1, 3, 5, 3, 0, -1, -5], '<1'), -2)

    def test_equals_22(self):
        self.assertEqual(average_if([1, 3, 5, 3, 0, -1, -5], '<>1'), 5 / 6.0)

    def test_equals_23(self):
        self.assertEqual(average_if([99, 95.5, 0, 83], '<>0'), 92.5)
