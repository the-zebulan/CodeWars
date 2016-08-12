import unittest

from katas.kyu_7.number_encrypting_cypher import cypher


class CypherTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(cypher('Hello World'), 'H3110 W0r1d')

    def test_equal_2(self):
        self.assertEqual(cypher('I am your father'), '1 4m y0ur f47h3r')

    def test_equal_3(self):
        self.assertEqual(cypher(
            'I do not know what else I can test. Be cool. Good luck'
        ), '1 d0 n07 kn0w wh47 3153 1 c4n 7357. 83 c001. 600d 1uck')

    def test_equal_4(self):
        self.assertEqual(cypher('IlRzEeAaSsGbTtBgOo'), '112233445566778900')

    def test_equal_5(self):
        self.assertEqual(cypher(''), '')
