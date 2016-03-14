import unittest

from katas.kyu_6.collatz import collatz


class CollatzTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(collatz(4), '4->2->1')

    def test_equals_2(self):
        self.assertEqual(collatz(3), '3->10->5->16->8->4->2->1')


if __name__ == '__main__':
    unittest.main()
