import unittest

from Kyu_7.distance_from_the_average import distances_from_average


class DistancesFromTheAverageTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(distances_from_average([55, 95, 62, 36, 48]),
                         [4.2, -35.8, -2.8, 23.2, 11.2])

    def test_equals_2(self):
        self.assertEqual(distances_from_average([1, 1, 1, 1, 1]),
                         [0, 0, 0, 0, 0])

    def test_equals_3(self):
        self.assertEqual(distances_from_average([1, -1, 1, -1, 1, -1]),
                         [-1.0, 1.0, -1.0, 1.0, -1.0, 1.0])

    def test_equals_4(self):
        self.assertEqual(distances_from_average([1, -1, 1, -1, 1]),
                         [-0.8, 1.2, -0.8, 1.2, -0.8])

    def test_equals_5(self):
        self.assertEqual(distances_from_average([2, -2]), [-2.0, 2.0])

    def test_equals_6(self):
        self.assertEqual(distances_from_average([1]), [0])

    def test_equals_7(self):
        self.assertEqual(distances_from_average(
            [123, -65, 32432, -353, -534]
        ), [6197.6, 6385.6, -26111.4, 6673.6, 6854.6])

    def test_equals_8(self):
        self.assertEqual(distances_from_average(xrange(101)),
                         range(50, -51, -1))

    def test_equals_9(self):
        self.assertEqual(distances_from_average(xrange(1001)),
                         range(500, -501, -1))

    def test_equals_10(self):
        self.assertEqual(distances_from_average(xrange(1000001)),
                         range(500000, -500001, -1))


if __name__ == '__main__':
    unittest.main()
