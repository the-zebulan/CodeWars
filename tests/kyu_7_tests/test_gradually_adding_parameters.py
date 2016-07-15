import unittest

from katas.kyu_7.gradually_adding_parameters import add


class AddingParametersTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(add(), 0)

    def test_equals_2(self):
        self.assertEqual(add(100, 200, 300), 1400)

    def test_equals_3(self):
        self.assertEqual(add(2), 2)
