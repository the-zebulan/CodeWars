import unittest

from kyu_7.functional_addition import add


class AddTestCase(unittest.TestCase):
    def test_equals(self):
        add_one = add(1)
        self.assertEqual(add_one(3), 4)

    def test_equals_2(self):
        add_three = add(3)
        self.assertEqual(add_three(3), 6)


if __name__ == '__main__':
    unittest.main()
