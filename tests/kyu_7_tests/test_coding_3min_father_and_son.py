import unittest

from katas.kyu_7.coding_3min_father_and_son import sc


class FatherAndSonTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sc('AaaaAaab'), 'AaaaAaa')

    def test_equals_2(self):
        self.assertEqual(sc('aAAAaAAb'), 'aAAAaAA')

    def test_equals_3(self):
        self.assertEqual(sc('Aab'), 'Aa')

    def test_equals_4(self):
        self.assertEqual(sc('AabBc'), 'AabB')

    def test_equals_5(self):
        self.assertEqual(sc('SONson'), 'SONson')

    def test_equals_6(self):
        self.assertEqual(sc('FfAaTtHhEeRr'), 'FfAaTtHhEeRr')

    def test_equals_7(self):
        self.assertEqual(sc('SONsonfather'), 'SONson')

    def test_equals_8(self):
        self.assertEqual(sc('sonfather'), '')

    def test_equals_9(self):
        self.assertEqual(sc('DONKEYmonkey'), 'ONKEYonkey')

    def test_equals_10(self):
        self.assertEqual(sc('monkeyDONKEY'), 'onkeyONKEY')

    def test_equals_11(self):
        self.assertEqual(sc('BANAna'), 'ANAna')
