# coding=utf-8
import unittest

from Kyu_6.l33t_greek_case import gr33k_l33t


class GreekTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(gr33k_l33t('CodeWars'), 'cθδεωαπs')

    def test_equals_2(self):
        self.assertEqual(gr33k_l33t('Kata'), 'κατα')


if __name__ == '__main__':
    unittest.main()
