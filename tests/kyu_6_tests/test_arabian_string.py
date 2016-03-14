import unittest

from katas.kyu_6.arabian_string import camelize


class CamelizeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(camelize('java script'), 'JavaScript')

    def test_equals_2(self):
        self.assertEqual(camelize('cODE warS'), 'CodeWars')

    def test_equals_3(self):
        self.assertEqual(camelize('Rugby:Club:2013'), 'RugbyClub2013')


if __name__ == '__main__':
    unittest.main()
