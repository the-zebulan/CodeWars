import unittest

from Kyu_7.caffeine_script import caffeineBuzz


class CaffeineBuzzTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(caffeineBuzz(1), 'mocha_missing!')

    def test_equals_2(self):
        self.assertEqual(caffeineBuzz(3), 'Java')

    def test_equals_3(self):
        self.assertEqual(caffeineBuzz(6), 'JavaScript')

    def test_equals_4(self):
        self.assertEqual(caffeineBuzz(12), 'CoffeeScript')


if __name__ == '__main__':
    unittest.main()
