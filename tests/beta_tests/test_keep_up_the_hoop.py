import unittest

from beta.keep_up_the_hoop import hoopCount


class HoopCountTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(hoopCount(3), 'Keep at it until you get it')

    def test_equals_2(self):
        self.assertEqual(hoopCount(11), 'Great, now move on to tricks')


if __name__ == '__main__':
    unittest.main()
