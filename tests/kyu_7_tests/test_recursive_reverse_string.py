import unittest

from katas.kyu_7.recursive_reverse_string import reverse


class ReverseTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(reverse('abc'), 'cba')

    def test_equals_2(self):
        self.assertEqual(reverse('dlrow olleh'), 'hello world')


if __name__ == '__main__':
    unittest.main()
