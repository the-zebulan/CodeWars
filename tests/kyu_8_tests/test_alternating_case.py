import unittest

from katas.kyu_8.alternating_case import to_alternating_case


class AlternatingCaseTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(to_alternating_case('hello world'), 'HELLO WORLD')

    def test_equals_2(self):
        self.assertEqual(to_alternating_case('HELLO WORLD'), 'hello world')

    def test_equals_3(self):
        self.assertEqual(to_alternating_case('hello WORLD'), 'HELLO world')

    def test_equals_4(self):
        self.assertEqual(to_alternating_case('HeLLo WoRLD'), 'hEllO wOrld')

    def test_equals_5(self):
        self.assertEqual(to_alternating_case('12345'), '12345')

    def test_equals_6(self):
        self.assertEqual(to_alternating_case('1a2b3c4d5e'), '1A2B3C4D5E')

    def test_equals_7(self):
        self.assertEqual(
            to_alternating_case('String.prototype.toAlternatingCase'),
            'sTRING.PROTOTYPE.TOaLTERNATINGcASE'
        )

    def test_equals_8(self):
        self.assertEqual(
            to_alternating_case(to_alternating_case('Hello World')),
            'Hello World'
        )

    def test_equals_9(self):
        self.assertEqual(
            to_alternating_case('altERnaTIng cAsE'), 'ALTerNAtiNG CaSe'
        )

    def test_equals_10(self):
        self.assertEqual(
            to_alternating_case('altERnaTIng cAsE <=> ALTerNAtiNG CaSe'),
            'ALTerNAtiNG CaSe <=> altERnaTIng cAsE'
        )

    def test_equals_11(self):
        self.assertEqual(
            to_alternating_case('ALTerNAtiNG CaSe <=> altERnaTIng cAsE'),
            'altERnaTIng cAsE <=> ALTerNAtiNG CaSe'
        )
