import unittest

from kyu_7.area_of_a_circle import circleArea


class CircleAreaTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(circleArea(43.2673), 5881.25)

    def test_equals_2(self):
        self.assertEqual(circleArea(68), 14526.72)

    def test_false(self):
        self.assertFalse(circleArea(-1485.86))

    def test_false_2(self):
        self.assertFalse(circleArea(0))

    def test_false_3(self):
        self.assertFalse(circleArea('number'))


if __name__ == '__main__':
    unittest.main()
