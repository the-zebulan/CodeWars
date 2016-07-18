import unittest

from katas.kyu_6.summarize_ranges import summary_ranges


class SummarizeRangesTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(summary_ranges([1, 1, 1, 1]), ['1'])

    def test_equal_2(self):
        self.assertEqual(summary_ranges([1, 2, 3, 4]), ['1->4'])

    def test_equal_3(self):
        self.assertEqual(summary_ranges([0, 1, 2, 5, 6, 9]),
                         ['0->2', '5->6', '9'])

    def test_equal_4(self):
        self.assertEqual(summary_ranges([0, 1, 2, 3, 3, 3, 4, 5, 6, 7]),
                         ['0->7'])

    def test_equal_5(self):
        self.assertEqual(summary_ranges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7]),
                         ['0->7'])

    def test_equal_6(self):
        self.assertEqual(summary_ranges([]), [])

    def test_equal_7(self):
        self.assertEqual(summary_ranges(None), [])
