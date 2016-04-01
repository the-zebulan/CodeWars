import unittest

from katas.kyu_8.my_head_is_at_the_wrong_end import fix_the_meerkat


class FixTheMeerkatTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(
            fix_the_meerkat(['tail', 'body', 'head']),
            ['head', 'body', 'tail']
        )

    def test_equals_2(self):
        self.assertEqual(
            fix_the_meerkat(['tails', 'body', 'heads']),
            ['heads', 'body', 'tails']
        )

    def test_equals_3(self):
        self.assertEqual(
            fix_the_meerkat(['bottom', 'middle', 'top']),
            ['top', 'middle', 'bottom']
        )

    def test_equals_4(self):
        self.assertEqual(
            fix_the_meerkat(['lower legs', 'torso', 'upper legs']),
            ['upper legs', 'torso', 'lower legs']
        )

    def test_equals_5(self):
        self.assertEqual(
            fix_the_meerkat(['ground', 'rainbow', 'sky']),
            ['sky', 'rainbow', 'ground']
        )


if __name__ == '__main__':
    unittest.main()
