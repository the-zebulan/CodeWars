import unittest

from katas.beta.bubble_sort import bubble


class BubbleSortTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(bubble([]), [])

    def test_equal_2(self):
        self.assertEqual(bubble([628]), [])

    def test_equal_3(self):
        self.assertEqual(bubble([1, 2, 4, 3]), [[1, 2, 3, 4]])

    def test_equal_4(self):
        self.assertEqual(bubble([2, 1, 4, 3]), [[1, 2, 4, 3], [1, 2, 3, 4]])

    def test_equal_5(self):
        self.assertEqual(bubble([1, 4, 3, 6, 7, 9, 2, 5, 8]), [
            [1, 3, 4, 6, 7, 9, 2, 5, 8],
            [1, 3, 4, 6, 7, 2, 9, 5, 8],
            [1, 3, 4, 6, 7, 2, 5, 9, 8],
            [1, 3, 4, 6, 7, 2, 5, 8, 9],
            [1, 3, 4, 6, 2, 7, 5, 8, 9],
            [1, 3, 4, 6, 2, 5, 7, 8, 9],
            [1, 3, 4, 2, 6, 5, 7, 8, 9],
            [1, 3, 4, 2, 5, 6, 7, 8, 9],
            [1, 3, 2, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ])

    def test_equal_6(self):
        self.assertEqual(bubble([1, 2, 3, 4, 5, 6, 7, 8, 9]), [])

    def test_equal_7(self):
        self.assertEqual(bubble([1, 3, 3, 7, 4, 2]), [
            [1, 3, 3, 4, 7, 2],
            [1, 3, 3, 4, 2, 7],
            [1, 3, 3, 2, 4, 7],
            [1, 3, 2, 3, 4, 7],
            [1, 2, 3, 3, 4, 7]
        ])

    def test_equal_8(self):
        self.assertEqual(bubble(
            [145, 625, 353, 922, 613, 785, 482, 730, 931, 316]
        ), [[145, 353, 625, 922, 613, 785, 482, 730, 931, 316],
            [145, 353, 625, 613, 922, 785, 482, 730, 931, 316],
            [145, 353, 625, 613, 785, 922, 482, 730, 931, 316],
            [145, 353, 625, 613, 785, 482, 922, 730, 931, 316],
            [145, 353, 625, 613, 785, 482, 730, 922, 931, 316],
            [145, 353, 625, 613, 785, 482, 730, 922, 316, 931],
            [145, 353, 613, 625, 785, 482, 730, 922, 316, 931],
            [145, 353, 613, 625, 482, 785, 730, 922, 316, 931],
            [145, 353, 613, 625, 482, 730, 785, 922, 316, 931],
            [145, 353, 613, 625, 482, 730, 785, 316, 922, 931],
            [145, 353, 613, 482, 625, 730, 785, 316, 922, 931],
            [145, 353, 613, 482, 625, 730, 316, 785, 922, 931],
            [145, 353, 482, 613, 625, 730, 316, 785, 922, 931],
            [145, 353, 482, 613, 625, 316, 730, 785, 922, 931],
            [145, 353, 482, 613, 316, 625, 730, 785, 922, 931],
            [145, 353, 482, 316, 613, 625, 730, 785, 922, 931],
            [145, 353, 316, 482, 613, 625, 730, 785, 922, 931],
            [145, 316, 353, 482, 613, 625, 730, 785, 922, 931]]
        )

    def test_equal_9(self):
        self.assertEqual(bubble(
            [397, 668, 496, 311, 287, 152, 564, 482, 597]
        ), [[397, 496, 668, 311, 287, 152, 564, 482, 597],
            [397, 496, 311, 668, 287, 152, 564, 482, 597],
            [397, 496, 311, 287, 668, 152, 564, 482, 597],
            [397, 496, 311, 287, 152, 668, 564, 482, 597],
            [397, 496, 311, 287, 152, 564, 668, 482, 597],
            [397, 496, 311, 287, 152, 564, 482, 668, 597],
            [397, 496, 311, 287, 152, 564, 482, 597, 668],
            [397, 311, 496, 287, 152, 564, 482, 597, 668],
            [397, 311, 287, 496, 152, 564, 482, 597, 668],
            [397, 311, 287, 152, 496, 564, 482, 597, 668],
            [397, 311, 287, 152, 496, 482, 564, 597, 668],
            [311, 397, 287, 152, 496, 482, 564, 597, 668],
            [311, 287, 397, 152, 496, 482, 564, 597, 668],
            [311, 287, 152, 397, 496, 482, 564, 597, 668],
            [311, 287, 152, 397, 482, 496, 564, 597, 668],
            [287, 311, 152, 397, 482, 496, 564, 597, 668],
            [287, 152, 311, 397, 482, 496, 564, 597, 668],
            [152, 287, 311, 397, 482, 496, 564, 597, 668]]
        )

    def test_equal_10(self):
        self.assertEqual(bubble(
            [816, 696, 617, 809, 759, 164, 71, 56, 473]
        ), [[696, 816, 617, 809, 759, 164, 71, 56, 473],
            [696, 617, 816, 809, 759, 164, 71, 56, 473],
            [696, 617, 809, 816, 759, 164, 71, 56, 473],
            [696, 617, 809, 759, 816, 164, 71, 56, 473],
            [696, 617, 809, 759, 164, 816, 71, 56, 473],
            [696, 617, 809, 759, 164, 71, 816, 56, 473],
            [696, 617, 809, 759, 164, 71, 56, 816, 473],
            [696, 617, 809, 759, 164, 71, 56, 473, 816],
            [617, 696, 809, 759, 164, 71, 56, 473, 816],
            [617, 696, 759, 809, 164, 71, 56, 473, 816],
            [617, 696, 759, 164, 809, 71, 56, 473, 816],
            [617, 696, 759, 164, 71, 809, 56, 473, 816],
            [617, 696, 759, 164, 71, 56, 809, 473, 816],
            [617, 696, 759, 164, 71, 56, 473, 809, 816],
            [617, 696, 164, 759, 71, 56, 473, 809, 816],
            [617, 696, 164, 71, 759, 56, 473, 809, 816],
            [617, 696, 164, 71, 56, 759, 473, 809, 816],
            [617, 696, 164, 71, 56, 473, 759, 809, 816],
            [617, 164, 696, 71, 56, 473, 759, 809, 816],
            [617, 164, 71, 696, 56, 473, 759, 809, 816],
            [617, 164, 71, 56, 696, 473, 759, 809, 816],
            [617, 164, 71, 56, 473, 696, 759, 809, 816],
            [164, 617, 71, 56, 473, 696, 759, 809, 816],
            [164, 71, 617, 56, 473, 696, 759, 809, 816],
            [164, 71, 56, 617, 473, 696, 759, 809, 816],
            [164, 71, 56, 473, 617, 696, 759, 809, 816],
            [71, 164, 56, 473, 617, 696, 759, 809, 816],
            [71, 56, 164, 473, 617, 696, 759, 809, 816],
            [56, 71, 164, 473, 617, 696, 759, 809, 816]]
        )

    def test_equal_11(self):
        self.assertEqual(bubble(
            [554, 113, 227, 466, 630, 482, 977, 543, 588]
        ), [[113, 554, 227, 466, 630, 482, 977, 543, 588],
            [113, 227, 554, 466, 630, 482, 977, 543, 588],
            [113, 227, 466, 554, 630, 482, 977, 543, 588],
            [113, 227, 466, 554, 482, 630, 977, 543, 588],
            [113, 227, 466, 554, 482, 630, 543, 977, 588],
            [113, 227, 466, 554, 482, 630, 543, 588, 977],
            [113, 227, 466, 482, 554, 630, 543, 588, 977],
            [113, 227, 466, 482, 554, 543, 630, 588, 977],
            [113, 227, 466, 482, 554, 543, 588, 630, 977],
            [113, 227, 466, 482, 543, 554, 588, 630, 977]]
        )

    def test_equal_12(self):
        self.assertEqual(bubble(
            [237, 316, 35, 641, 189, 318, 804]
        ), [[237, 35, 316, 641, 189, 318, 804],
            [237, 35, 316, 189, 641, 318, 804],
            [237, 35, 316, 189, 318, 641, 804],
            [35, 237, 316, 189, 318, 641, 804],
            [35, 237, 189, 316, 318, 641, 804],
            [35, 189, 237, 316, 318, 641, 804]]
        )
