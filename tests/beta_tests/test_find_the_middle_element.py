import unittest

from beta.find_the_middle_element import gimme


class GimmeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(gimme([2, 3, 1]), 0)

    def test_equals_2(self):
        self.assertEqual(gimme([5, 10, 14]), 1)


if __name__ == '__main__':
    unittest.main()
