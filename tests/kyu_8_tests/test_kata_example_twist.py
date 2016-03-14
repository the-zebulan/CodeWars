import unittest

from kyu_8.kata_example_twist import websites


class WebsitesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(len(websites), 1000)

    def test_equals_2(self):
        self.assertEqual(websites.count('codewars'), 1000)


if __name__ == '__main__':
    unittest.main()
