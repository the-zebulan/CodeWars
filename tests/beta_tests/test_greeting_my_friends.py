import unittest

from katas.beta.greeting_my_friends import greeting_for_all_friends


class GreetingTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(greeting_for_all_friends(['Bilal']), ['Hello, Bilal!'])

    def test_none(self):
        self.assertIsNone(greeting_for_all_friends(None))

    def test_none_2(self):
        self.assertIsNone(greeting_for_all_friends([]))


if __name__ == '__main__':
    unittest.main()
