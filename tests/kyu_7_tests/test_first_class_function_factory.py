import unittest

from katas.kyu_7.first_class_function_factory import factory


class FactoryTestCase(unittest.TestCase):
    def setUp(self):
        self.my_arr = [1, 2, 3]

    def test_equals(self):
        threes = factory(3)
        self.assertEqual(threes(self.my_arr), [3, 6, 9])

    def test_equals_2(self):
        fives = factory(5)
        self.assertEqual(fives(self.my_arr), [5, 10, 15])
