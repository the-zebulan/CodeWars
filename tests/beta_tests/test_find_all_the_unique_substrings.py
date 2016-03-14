import unittest

from katas.beta.find_all_the_unique_substrings import getSubstrings


class GetSubstringsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(getSubstrings('YOLO'), 9)

    def test_equals_2(self):
        self.assertEqual(getSubstrings(
            'I am but a string in the meadow.'), 511)


if __name__ == '__main__':
    unittest.main()
