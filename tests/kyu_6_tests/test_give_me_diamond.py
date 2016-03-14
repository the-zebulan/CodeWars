import unittest

from kyu_6.give_me_diamond import diamond


class DiamondTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(diamond(3), ' *\n***\n *\n')

    def test_none(self):
        self.assertIsNone(diamond(6))

    def test_none_2(self):
        self.assertIsNone(diamond(-1))


if __name__ == '__main__':
    unittest.main()
