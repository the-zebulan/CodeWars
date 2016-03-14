import unittest

from Kyu_6.title_case import title_case


class TitleCaseTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(title_case('a bc', 'bc'), 'A bc')

    def test_equals_2(self):
        self.assertEqual(title_case(''), '')

    def test_equals_3(self):
        self.assertEqual(title_case('a clash of KINGS', 'a an the of'),
                         'A Clash of Kings')

    def test_equals_4(self):
        self.assertEqual(title_case('THE WIND IN THE WILLOWS', 'The In'),
                         'The Wind in the Willows')

    def test_equals_5(self):
        self.assertEqual(title_case('the quick brown fox'),
                         'The Quick Brown Fox')


if __name__ == '__main__':
    unittest.main()
