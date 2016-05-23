import unittest

from katas.kyu_7.gauss_needs_help import f


class GaussTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(f(100), 5050)

    def test_equal_2(self):
        self.assertEqual(f(300), 45150)

    def test_equal_3(self):
        self.assertEqual(f(303), 46056)

    def test_equal_4(self):
        self.assertEqual(f(50000), 1250025000)

    def test_is_none_1(self):
        self.assertIsNone(f('n'))

    def test_is_none_2(self):
        self.assertIsNone(f(3.14))

    def test_is_none_3(self):
        self.assertIsNone(f(0))

    def test_is_none_4(self):
        self.assertIsNone(f(-10))

    def test_is_none_5(self):
        self.assertIsNone(f(None))


if __name__ == '__main__':
    unittest.main()
