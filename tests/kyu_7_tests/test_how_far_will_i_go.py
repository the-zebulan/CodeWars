import unittest

from Kyu_7.how_far_will_i_go import travel


class TravelTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(travel(1000, 10, 127, 14), 1120)

    def test_equals_2(self):
        self.assertEqual(travel(1000, 10, 0, 10), 10000)

    def test_equals_3(self):
        self.assertEqual(travel(25, 50, 120, 18), 450)

    def test_equals_4(self):
        self.assertEqual(travel(35869784, 90, 100, 5), 84954920)

    def test_equals_5(self):
        self.assertEqual(travel(1234567, 4, 3, 11), 7760148)

    def test_equals_6(self):
        self.assertEqual(travel(100000000, 21, 5, 14), 1130769276)

    def test_equals_7(self):
        self.assertEqual(travel(0, 100, 10, 14), 0)

    def test_equals_8(self):
        self.assertEqual(travel(250, 0, 5, 14), 0)

    def test_equals_9(self):
        self.assertEqual(travel(100, 10, 0, 14), 1400)

    def test_equals_10(self):
        self.assertEqual(travel(500, 100, 10, 0), 0)


if __name__ == '__main__':
    unittest.main()
