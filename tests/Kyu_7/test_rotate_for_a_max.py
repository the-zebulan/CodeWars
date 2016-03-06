import unittest

from Kyu_7.rotate_for_a_max import max_rot


class MaximumRotationTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(max_rot(56789), 68957)

    def test_equals_2(self):
        self.assertEqual(max_rot(38458215), 85821534)

    def test_equals_3(self):
        self.assertEqual(max_rot(195881031), 988103115)

    def test_equals_4(self):
        self.assertEqual(max_rot(896219342), 962193428)

    def test_equals_5(self):
        self.assertEqual(max_rot(69418307), 94183076)


if __name__ == '__main__':
    unittest.main()
