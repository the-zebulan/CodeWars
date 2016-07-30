import unittest

from katas.beta.name_that_number import name_that_number


class NameThatNumberTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(name_that_number(0), 'zero')

    def test_equal_2(self):
        self.assertEqual(name_that_number(1), 'one')

    def test_equal_3(self):
        self.assertEqual(name_that_number(4), 'four')

    def test_equal_4(self):
        self.assertEqual(name_that_number(9), 'nine')

    def test_equal_5(self):
        self.assertEqual(name_that_number(21), 'twenty one')

    def test_equal_6(self):
        self.assertEqual(name_that_number(23), 'twenty three')

    def test_equal_7(self):
        self.assertEqual(name_that_number(52), 'fifty two')

    def test_equal_8(self):
        self.assertEqual(name_that_number(53), 'fifty three')

    def test_equal_9(self):
        self.assertEqual(name_that_number(76), 'seventy six')

    def test_equal_10(self):
        self.assertEqual(name_that_number(99), 'ninety nine')
