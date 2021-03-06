import unittest

from katas.kyu_7.case_swapping import swap


class CaseSwappingTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(swap('HelloWorld'), 'hELLOwORLD')

    def test_equals_2(self):
        self.assertEqual(swap('CodeWars'), 'cODEwARS')
