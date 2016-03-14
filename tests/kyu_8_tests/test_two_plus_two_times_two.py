import unittest

from katas.kyu_8.two_plus_two_times_two import calculate


class CalculateTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(calculate(), 8)


if __name__ == '__main__':
    unittest.main()
