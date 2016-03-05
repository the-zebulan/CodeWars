import unittest

from Kyu_6.what_will_be_the_odd_one_out import odd_one_out


class OddOneOutTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(odd_one_out('Hello World'),
                         ['H', 'e', ' ', 'W', 'r', 'l', 'd'])

    def test_equals_2(self):
        self.assertEqual(odd_one_out('Codewars'),
                         ['C', 'o', 'd', 'e', 'w', 'a', 'r', 's'])

    def test_equals_3(self):
        self.assertEqual(odd_one_out('woowee'), [])

    def test_equals_4(self):
        self.assertEqual(odd_one_out('wwoooowweeee'), [])

    def test_equals_5(self):
        self.assertEqual(odd_one_out('racecar'), ['e'])

    def test_equals_6(self):
        self.assertEqual(odd_one_out('Mamma'), ['M'])

    def test_equals_7(self):
        self.assertEqual(odd_one_out('Mama'), ['M', 'm'])


if __name__ == '__main__':
    unittest.main()
