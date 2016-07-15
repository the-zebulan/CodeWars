import unittest

from katas.kyu_7.the_barksdale_code import decode


class BarksdaleCodeTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(decode('4103432323'), '6957678787')

    def test_equal_2(self):
        self.assertEqual(decode('4103438970'), '6957672135')

    def test_equal_3(self):
        self.assertEqual(decode('4104305768'), '6956750342')

    def test_equal_4(self):
        self.assertEqual(decode('4102204351'), '6958856709')

    def test_equal_5(self):
        self.assertEqual(decode('4107056043'), '6953504567')
