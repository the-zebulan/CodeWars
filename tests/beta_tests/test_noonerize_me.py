import unittest

from katas.beta.noonerize_me import noonerize


class NoonerizeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(noonerize([12, 34]), 18)

    def test_equals_2(self):
        self.assertEqual(noonerize([55, 63]), 12)

    def test_equals_3(self):
        self.assertEqual(noonerize([357, 579]), 178)

    def test_equals_4(self):
        self.assertEqual(noonerize([1000000, 9999999]), 7000001)

    def test_equals_5(self):
        self.assertEqual(noonerize([1000000, 'hello']), 'invalid array')

    def test_equals_6(self):
        self.assertEqual(noonerize(['pippi', 9999999]), 'invalid array')

    def test_equals_7(self):
        self.assertEqual(noonerize(['pippi', 'hello']), 'invalid array')

    def test_equals_8(self):
        self.assertEqual(noonerize([1, 1]), 0)

    def test_equals_9(self):
        self.assertEqual(noonerize([1, 0]), 1)

    def test_equals_10(self):
        self.assertEqual(noonerize([0, 1]), 1)


if __name__ == '__main__':
    unittest.main()
