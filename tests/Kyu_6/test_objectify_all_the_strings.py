import unittest

from Kyu_6.objectify_all_the_strings import hashify


class HashifyTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(hashify('123456'), {
            '1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6': '1'
        })

    def test_equals_2(self):
        self.assertEqual(hashify('11223'),
                         {'1': ['1', '2'], '2': ['2', '3'], '3': '1'})

    def test_equals_3(self):
        self.assertEqual(hashify('Codewars'), {
            'C': 'o', 'o': 'd', 'd': 'e', 'e': 'w', 'w': 'a', 'a': 'r',
            'r': 's', 's': 'C'})

    def test_equals_4(self):
        self.assertEqual(hashify('this is a string'), {
            't': ['h', 'r'], 'h': 'i', 'i': ['s', 's', 'n'],
            's': [' ', ' ', 't'], ' ': ['i', 'a', 's'], 'a': ' ', 'r': 'i',
            'n': 'g', 'g': 't'})

    def test_equals_5(self):
        self.assertEqual(hashify('racecar'), {
            'r': ['a', 'r'], 'a': ['c', 'r'], 'c': ['e', 'a'], 'e': 'c'})

    def test_equals_6(self):
        self.assertEqual(hashify('CcCcCcCc'), {
            'c': ['C', 'C', 'C', 'C'], 'C': ['c', 'c', 'c', 'c']})


if __name__ == '__main__':
    unittest.main()
