import unittest

from kyu_8.name_shuffler import name_shuffler


class NameShufflerTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(name_shuffler('john McClane'), 'McClane john')

    def test_equals_2(self):
        self.assertEqual(name_shuffler('Mary jeggins'), 'jeggins Mary')

    def test_equals_3(self):
        self.assertEqual(name_shuffler('tom jerry'), 'jerry tom')


if __name__ == '__main__':
    unittest.main()
