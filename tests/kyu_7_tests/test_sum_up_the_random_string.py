import unittest

from katas.kyu_7.sum_up_the_random_string import sum_from_string


class SumFromStringTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sum_from_string(
            'In 2015, I want to know how much does iPhone 6+ cost?'), 2021)

    def test_equals_2(self):
        self.assertEqual(sum_from_string('1+1=2'), 4)

    def test_equals_3(self):
        self.assertEqual(sum_from_string('e=mc^2'), 2)
