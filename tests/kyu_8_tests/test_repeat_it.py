import unittest

from katas.kyu_8.repeat_it import repeat_it


class RepeatItTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(repeat_it('*', 3), '***')

    def test_equals_2(self):
        self.assertEqual(repeat_it(
            'Hello', 11
        ), 'HelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHello')
