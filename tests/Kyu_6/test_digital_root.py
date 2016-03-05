import unittest

from Kyu_6.digital_root import digital_root


class DigitalRootTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(digital_root(16), 7)

    def test_equals_2(self):
        self.assertEqual(digital_root(942), 6)

    def test_equals_3(self):
        self.assertEqual(digital_root(132189), 6)

    def test_equals_4(self):
        self.assertEqual(digital_root(493193), 2)


if __name__ == '__main__':
    unittest.main()
