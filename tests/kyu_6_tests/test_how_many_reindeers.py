import unittest

from Kyu_6.how_many_reindeers import reindeer


class ReindeerTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(reindeer(0), 2)

    def test_equals_2(self):
        self.assertEqual(reindeer(1), 3)

    def test_equals_3(self):
        self.assertEqual(reindeer(30), 3)

    def test_exception(self):
        self.assertRaises(AssertionError, reindeer, 200)


if __name__ == '__main__':
    unittest.main()
