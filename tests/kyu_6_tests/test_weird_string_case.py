import unittest

from katas.kyu_6.weird_string_case import to_weird_case


class WeirdStringCaseTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(to_weird_case('This'), 'ThIs')

    def test_equals_2(self):
        self.assertEqual(to_weird_case('is'), 'Is')

    def test_equals_3(self):
        self.assertEqual(to_weird_case('This is a test'), 'ThIs Is A TeSt')
