import unittest

from katas.kyu_7.two_to_one import longest


class LongestTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(longest('aretheyhere', 'yestheyarehere'), 'aehrsty')

    def test_equals_2(self):
        self.assertEqual(longest(
            'loopingisfunbutdangerous', 'lessdangerousthancoding'),
            'abcdefghilnoprstu')

    def test_equals_3(self):
        self.assertEqual(longest('inmanylanguages', 'theresapairoffunctions'),
                         'acefghilmnoprstuy')


if __name__ == '__main__':
    unittest.main()
