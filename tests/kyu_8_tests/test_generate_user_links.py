import unittest

from katas.kyu_8.generate_user_links import generate_link


class GenerateLinkTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(generate_link('matt c'),
                         'http://www.codewars.com/users/matt%20c')

    def test_equals_2(self):
        self.assertEqual(generate_link('g964'),
                         'http://www.codewars.com/users/g964')

    def test_equals_3(self):
        self.assertEqual(generate_link('GiacomoSorbi'),
                         'http://www.codewars.com/users/GiacomoSorbi')

    def test_equals_4(self):
        self.assertEqual(generate_link('ZozoFouchtra'),
                         'http://www.codewars.com/users/ZozoFouchtra')

    def test_equals_5(self):
        self.assertEqual(generate_link('colbydauph'),
                         'http://www.codewars.com/users/colbydauph')


if __name__ == '__main__':
    unittest.main()
