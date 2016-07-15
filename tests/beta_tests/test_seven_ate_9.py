import unittest

from katas.beta.seven_ate_9 import seven_ate9


class SevenAteNineTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(seven_ate9('79797'), '777')

    def test_equals_2(self):
        self.assertEqual(seven_ate9('12345'), '12345')
