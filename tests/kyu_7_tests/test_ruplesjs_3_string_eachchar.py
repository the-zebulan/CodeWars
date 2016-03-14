import unittest

from kyu_7.ruplesjs_3_string_eachchar import each_char


class EachCharacterTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(each_char('hello', ' '), 'h e l l o ')

    def test_equals_2(self):
        self.assertEqual(each_char('hello', '123'), 'h123e123l123l123o123')

    def test_equals_3(self):
        self.assertEqual(each_char('', '123'), '')

    def test_equals_4(self):
        self.assertEqual(each_char('hello', lambda c: c.upper()), 'HELLO')

    def test_equals_5(self):
        self.assertEqual(each_char(
            'H e l l o ', lambda c: '1' if c == ' ' else c), 'H1e1l1l1o1')

    def test_equals_6(self):
        self.assertEqual(each_char(
            'I12 0ca431n35no55t 77re3321231ad 4t4h7771i888973s.',
            lambda c: '' if c in '0123456789' else c
        ), 'I cannot read this.')


if __name__ == '__main__':
    unittest.main()
