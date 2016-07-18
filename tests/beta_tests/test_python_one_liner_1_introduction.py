import unittest

from katas.beta.python_one_liner_1_introduction import (
    a, a_simple_function, my_list, lowercase_to_uppercase, path
)


class PythonOneLinerTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(a, 42)

    def test_equal_2(self):
        self.assertEqual(a_simple_function(1, 2, (3, 4)),
                         "I'm simple enough!")

    def test_equal_3(self):
        self.assertEqual(my_list, [
            '',
            'A',
            'AA',
            'AAA',
            'AAAA',
            'AAAAAA',
            'AAAAAAA',
            'AAAAAAAA',
            'AAAAAAAAA'
        ])

    def test_equal_4(self):
        self.assertEqual(lowercase_to_uppercase, {
            'a': 'A',
            'b': 'B',
            'c': 'C',
            'd': 'D',
            'e': 'E',
            'f': 'F',
            'g': 'G',
            'h': 'H',
            'i': 'I',
            'j': 'J',
            'k': 'K',
            'l': 'L',
            'm': 'M',
            'n': 'N',
            'o': 'O',
            'p': 'P',
            'q': 'Q',
            'r': 'R',
            's': 'S',
            't': 'T',
            'u': 'U',
            'v': 'V',
            'w': 'W',
            'x': 'X',
            'y': 'Y',
            'z': 'Z'
        })

    def test_equal_5(self):
        self.assertEqual(path, '/usr/bin')
