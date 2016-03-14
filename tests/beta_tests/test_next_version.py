import unittest

from katas.beta.next_version import next_version


class NextVersionTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(next_version('1.2.3'), '1.2.4')

    def test_equals_2(self):
        self.assertEqual(next_version('0.9.9'), '1.0.0')

    def test_equals_3(self):
        self.assertEqual(next_version('1'), '2')

    def test_equals_4(self):
        self.assertEqual(next_version('1.2.3.4.5.6.7.8'), '1.2.3.4.5.6.7.9')

    def test_equals_5(self):
        self.assertEqual(next_version('9.9'), '10.0')


if __name__ == '__main__':
    unittest.main()
