import unittest

from katas.beta.quicksum import quicksum


class QuicksumTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(quicksum('ACM'), 46)

    def test_equals_2(self):
        self.assertEqual(quicksum('A C M'), 75)

    def test_equals_3(self):
        self.assertEqual(quicksum('AbqTH #5'), 0)


if __name__ == '__main__':
    unittest.main()
