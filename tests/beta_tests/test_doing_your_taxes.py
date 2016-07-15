import unittest

from katas.beta.doing_your_taxes import tax


class TaxTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(tax(1.2), 1.26)

    def test_equals_2(self):
        self.assertEqual(tax(100), 105)

    def test_equals_3(self):
        self.assertEqual(tax('Hello'), 'Error 404')
