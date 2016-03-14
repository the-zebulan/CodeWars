import unittest

from katas.kyu_6.number_shortening_filter import shorten_number


class ShortenNumberTestCase(unittest.TestCase):
    def setUp(self):
        self.filter1 = shorten_number(['', 'k', 'm'], 1000)
        self.filter2 = shorten_number(['B', 'KB', 'MB', 'GB'], 1024)

    def test_equals(self):
        self.assertEqual(self.filter1('234324'), '234k')

    def test_equals_2(self):
        self.assertEqual(self.filter1('98234324'), '98m')

    def test_equals_3(self):
        self.assertEqual(self.filter1([1, 2, 3]), '[1, 2, 3]')

    def test_equals_4(self):
        self.assertEqual(self.filter2('32'), '32B')

    def test_equals_5(self):
        self.assertEqual(self.filter2('2100'), '2KB')

    def test_equals_6(self):
        self.assertEqual(self.filter2('pippi'), 'pippi')


if __name__ == '__main__':
    unittest.main()
