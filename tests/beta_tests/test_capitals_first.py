import unittest

from beta.capitals_first import capitals_first


class CapitalsFirstTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(capitals_first(
            'hey You, Sort me Already!'), 'You, Sort Already! hey me')

    def test_equals_2(self):
        self.assertEqual(capitals_first(
            'sense Does to That Make you?'), 'Does That Make sense to you?')


if __name__ == '__main__':
    unittest.main()
