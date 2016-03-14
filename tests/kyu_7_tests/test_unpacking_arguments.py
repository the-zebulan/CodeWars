import unittest

from katas.kyu_7.unpacking_arguments import spread


class SpreadTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(spread(lambda x, y: x + y, [1, 2]), 3)
        # Equivalent: (lambda x, y: x + y)(1, 2)


if __name__ == '__main__':
    unittest.main()
