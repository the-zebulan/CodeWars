import unittest

from katas.kyu_8.noob_code_1_supersize_me import super_size


class SuperSizeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(super_size(69), 96)

    def test_equals_2(self):
        self.assertEqual(super_size(513), 531)

    def test_equals_3(self):
        self.assertEqual(super_size(2017), 7210)

    def test_equals_4(self):
        self.assertEqual(super_size(414), 441)

    def test_equals_5(self):
        self.assertEqual(super_size(608719), 987610)

    def test_equals_6(self):
        self.assertEqual(super_size(123456789), 987654321)

    def test_equals_7(self):
        self.assertEqual(super_size(700000000001), 710000000000)

    def test_equals_8(self):
        self.assertEqual(super_size(666666), 666666)

    def test_equals_9(self):
        self.assertEqual(super_size(2), 2)

    def test_equals_10(self):
        self.assertEqual(super_size(0), 0)


if __name__ == '__main__':
    unittest.main()
