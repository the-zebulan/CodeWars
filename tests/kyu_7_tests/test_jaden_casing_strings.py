import unittest

from kyu_7.jaden_casing_strings import toJadenCase


class JadenCaseTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(toJadenCase(
            'How can mirrors be real if our eyes aren\'t real'
        ), 'How Can Mirrors Be Real If Our Eyes Aren\'t Real')


if __name__ == '__main__':
    unittest.main()
