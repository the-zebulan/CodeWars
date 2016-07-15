import unittest

from katas.kyu_8.one_hundred_and_one_dalmatians import how_many_dalmatians


class DalmatiansTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(how_many_dalmatians(26), 'More than a handful!')

    def test_equals_2(self):
        self.assertEqual(how_many_dalmatians(8), 'Hardly any')

    def test_equals_3(self):
        self.assertEqual(how_many_dalmatians(14), 'More than a handful!')

    def test_equals_4(self):
        self.assertEqual(how_many_dalmatians(80),
                         'Woah that\'s a lot of dogs!')

    def test_equals_5(self):
        self.assertEqual(how_many_dalmatians(100),
                         'Woah that\'s a lot of dogs!')

    def test_equals_6(self):
        self.assertEqual(how_many_dalmatians(50), 'More than a handful!')

    def test_equals_7(self):
        self.assertEqual(how_many_dalmatians(10), 'Hardly any')

    def test_equals_8(self):
        self.assertEqual(how_many_dalmatians(101), '101 DALMATIONS!!!')
