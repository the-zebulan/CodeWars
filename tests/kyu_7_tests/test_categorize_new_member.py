import unittest

from katas.kyu_7.categorize_new_member import openOrSenior


class OpenOrSeniorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(openOrSenior(
            [[45, 12], [55, 21], [19, -2], [104, 20]]
        ), ['Open', 'Senior', 'Open', 'Senior'])

    def test_equals_2(self):
        self.assertEqual(openOrSenior(
            [[16, 23], [73, 1], [56, 20], [1, -1]]
        ), ['Open', 'Open', 'Senior', 'Open'])
