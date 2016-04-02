import unittest

from katas.kyu_8.is_this_my_tail import correct_tail


class CorrectTailTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(correct_tail('Fox', 'x'))

    def test_true_2(self):
        self.assertTrue(correct_tail('Rhino', 'o'))

    def test_true_3(self):
        self.assertTrue(correct_tail('Meerkat', 't'))

    def test_false(self):
        self.assertFalse(correct_tail('Emu', 't'))

    def test_false_2(self):
        self.assertFalse(correct_tail('Badger', 's'))

    def test_false_3(self):
        self.assertFalse(correct_tail('Giraffe', 'd'))


if __name__ == '__main__':
    unittest.main()
