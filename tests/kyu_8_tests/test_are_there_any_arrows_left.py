import unittest

from katas.kyu_8.are_there_any_arrows_left import any_arrows


class ArrowsTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(any_arrows([
            {'range': 5}, {'range': 10, 'damaged': True}, {'damaged': True}
        ]))

    def test_true_2(self):
        self.assertTrue(any_arrows([
            {'range': 5}, {'range': 10, 'damaged': True}, {'damaged': True}
        ]))

    def test_false(self):
        self.assertFalse(any_arrows([
            {'range': 10, 'damaged': True}, {'damaged': True}
        ]))

    def test_false_2(self):
        self.assertFalse(any_arrows([]))


if __name__ == '__main__':
    unittest.main()
