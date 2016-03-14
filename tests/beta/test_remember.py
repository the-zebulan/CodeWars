import unittest

from Beta.remember import remember


class RememberTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(remember('apple'), ['p'])

    def test_equals_2(self):
        self.assertEqual(remember('apPle'), [])

    def test_equals_3(self):
        self.assertEqual(remember('pippi'), ['p', 'i'])

    def test_equals_4(self):
        self.assertEqual(remember('Pippi'), ['p', 'i'])

    def test_equals_5(self):
        self.assertEqual(remember('limbojackassin the garden'),
                         ['a', 's', 'i', ' ', 'e', 'n'])

    def test_equals_6(self):
        self.assertEqual(remember('11pinguin'), ['1', 'i', 'n'])


if __name__ == '__main__':
    unittest.main()
