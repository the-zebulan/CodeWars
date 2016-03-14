import unittest

from beta.first_character_that_repeats import first_dup


class FirstDuplicateTestCase(unittest.TestCase):
    def test_none(self):
        self.assertIsNone(first_dup('like'))

    def test_none_2(self):
        self.assertIsNone(first_dup('bar'))

    def test_equals(self):
        self.assertEqual(first_dup('tweet'), 't')

    def test_equals_2(self):
        self.assertEqual(first_dup('Ode to Joy'), ' ')

    def test_equals_3(self):
        self.assertEqual(first_dup('ode to joy'), 'o')

    def test_equals_4(self):
        self.assertEqual(first_dup('123123'), '1')

    def test_equals_5(self):
        self.assertEqual(first_dup('!@#$!@#$'), '!')

    def test_equals_6(self):
        self.assertEqual(first_dup('1a2b3a3c'), 'a')


if __name__ == '__main__':
    unittest.main()
