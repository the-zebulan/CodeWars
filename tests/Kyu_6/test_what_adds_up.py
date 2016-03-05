import unittest

from Kyu_6.what_adds_up import addsup


class WhatAddsUpTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(addsup([1, 2], [3, 1], [5, 4]),
                         [[1, 3, 4], [2, 3, 5]])


if __name__ == '__main__':
    unittest.main()
