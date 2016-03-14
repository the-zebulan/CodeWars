import unittest

from Beta.leonardo_dicaprio_and_oscars import leo


class LeonardoTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(leo(88), 'Leo finally won the oscar! Leo is happy')

    def test_equals_2(self):
        self.assertEqual(leo(86), 'Not even for Wolf of wallstreet?!')

    def test_equals_3(self):
        self.assertEqual(leo(20), 'When will you give Leo an Oscar?')

    def test_equals_4(self):
        self.assertEqual(leo(90), 'Leo got one already!')


if __name__ == '__main__':
    unittest.main()
