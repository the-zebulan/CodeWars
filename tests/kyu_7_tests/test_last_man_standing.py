import unittest

from katas.kyu_7.last_man_standing import last_man_standing


class LastManStandingTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(last_man_standing(9), 6)

    def test_equals_2(self):
        self.assertEqual(last_man_standing(10), 8)

    def test_equals_3(self):
        self.assertEqual(last_man_standing(100), 54)

    def test_equals_4(self):
        self.assertEqual(last_man_standing(1000), 510)


if __name__ == '__main__':
    unittest.main()
