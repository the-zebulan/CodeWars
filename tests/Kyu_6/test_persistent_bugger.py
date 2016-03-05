import unittest

from Kyu_6.persistent_bugger import persistence


class PersistenceTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(persistence(39), 3)

    def test_equals_2(self):
        self.assertEqual(persistence(4), 0)

    def test_equals_3(self):
        self.assertEqual(persistence(25), 2)

    def test_equals_4(self):
        self.assertEqual(persistence(999), 4)


if __name__ == '__main__':
    unittest.main()
