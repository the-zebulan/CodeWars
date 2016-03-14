import unittest

from katas.beta.only_readable_once_list import SecureList


class SecureListTestCase(unittest.TestCase):
    def setUp(self):
        self.base = [1, 2, 3, 4]

    def test_equals(self):
        a = SecureList(self.base)
        self.assertEqual(a[0], self.base[0])
        self.assertEqual(a[0], self.base[1])
        self.assertEqual(len(a), 2)
        print 'Current List: {!s}'.format(a)
        self.assertEqual(len(a), 0)

    def test_equals_2(self):
        b = SecureList(self.base)
        print 'Current List: {!r}'.format(b)
        self.assertEqual(len(b), 0)


if __name__ == '__main__':
    unittest.main()
