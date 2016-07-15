import unittest

from katas.kyu_7.reversing_fun import ReverseFun


class ReverseFunTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(ReverseFun('012345'), '504132')

    def test_equals_2(self):
        self.assertEqual(ReverseFun('jointhedarkside'), 'ejdoiisnktrhaed')
