import unittest

from katas.kyu_7.count_the_digit import nb_dig


class CountTheDigitTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(nb_dig(5750, 0), 4700)

    def test_equals_2(self):
        self.assertEqual(nb_dig(11011, 2), 9481)

    def test_equals_3(self):
        self.assertEqual(nb_dig(12224, 8), 7733)

    def test_equals_4(self):
        self.assertEqual(nb_dig(11549, 1), 11905)


if __name__ == '__main__':
    unittest.main()
