import unittest

from katas.beta.beginner_series_paperwork import paperwork


class PaperworkTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(paperwork(5, 5), 25)

    def test_equals_2(self):
        self.assertEqual(paperwork(-2, 10), 0)


if __name__ == '__main__':
    unittest.main()
