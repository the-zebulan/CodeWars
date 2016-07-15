import unittest

from katas.kyu_7.a_rule_of_divisibility_by_13 import thirt


class ThirtTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(thirt(1234567), 87)

    def test_equals_2(self):
        self.assertEqual(thirt(321), 48)

    def test_equals_3(self):
        self.assertEqual(thirt(8529), 79)

    def test_equals_4(self):
        self.assertEqual(thirt(85299258), 31)

    def test_equals_5(self):
        self.assertEqual(thirt(5634), 57)

    def test_equals_6(self):
        self.assertEqual(thirt(1111111111), 71)

    def test_equals_7(self):
        self.assertEqual(thirt(987654321), 30)
