import unittest

from Kyu_6.autocomplete_yay import autocomplete


class AutocompleteTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(autocomplete(
            'ai', ['airplane', 'airport', 'apple', 'ball']),
            ['airplane', 'airport'])

    def test_equals_2(self):
        self.assertEqual(autocomplete('ai', [
            'abnormal', 'arm-wrestling', 'absolute', 'airplane',
            'airport', 'amazing', 'apple', 'ball']),
            ['airplane', 'airport'])

    def test_equals_3(self):
        self.assertEqual(autocomplete('a', [
            'abnormal', 'arm-wrestling', 'absolute', 'airplane', 'airport',
            'amazing', 'apple', 'ball']), [
            'abnormal', 'arm-wrestling', 'absolute', 'airplane', 'airport'])


if __name__ == '__main__':
    unittest.main()
