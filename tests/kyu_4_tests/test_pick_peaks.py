import unittest

from katas.kyu_4.pick_peaks import pick_peaks


class PickPeaksTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(pick_peaks([1, 2, 2, 2, 3]),
                         {'pos': [], 'peaks': []})

    def test_equal_2(self):
        self.assertEqual(pick_peaks([0, 1, 2, 5, 1, 0]),
                         {'pos': [3], 'peaks': [5]})

    def test_equal_3(self):
        self.assertEqual(pick_peaks([1, 2, 2, 2, 1]),
                         {'pos': [1], 'peaks': [2]})

    def test_equal_4(self):
        self.assertEqual(pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]),
                         {'pos': [3, 7], 'peaks': [6, 3]})

    def test_equal_5(self):
        self.assertEqual(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]),
                         {'pos': [3, 7], 'peaks': [6, 3]})

    def test_equal_6(self):
        self.assertEqual(
            pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]),
            {'pos': [3, 7, 10], 'peaks': [6, 3, 2]})

    def test_equal_7(self):
        self.assertEqual(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2, 1]),
                         {'pos': [2, 4], 'peaks': [3, 2]})

    def test_equal_8(self):
        self.assertEqual(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2]),
                         {'pos': [2], 'peaks': [3]})
