import unittest

from Kyu_8.smallest_unused_id import next_id


class NextIDTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(next_id([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 11)

    def test_equals_2(self):
        self.assertEqual(next_id([5, 4, 3, 2, 1]), 0)

    def test_equals_3(self):
        self.assertEqual(next_id([0, 1, 2, 3, 5]), 4)

    def test_equals_4(self):
        self.assertEqual(next_id([0, 0, 0, 0, 0, 0]), 1)

    def test_equals_5(self):
        self.assertEqual(next_id([]), 0)


if __name__ == '__main__':
    unittest.main()
