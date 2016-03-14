import math
import unittest

import kyu_7.radians_to_degrees


class RadiansToDegreesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(math.degrees(math.pi), '180deg')

    def test_equals_2(self):
        self.assertEqual(math.radians(180), '3.14rad')


if __name__ == '__main__':
    unittest.main()
