import unittest

from katas.kyu_7.common_substrings import substring_test


class SubstringTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(substring_test('Something', 'Home'))

    def test_true_2(self):
        self.assertTrue(substring_test('BANANA', 'banana'))

    def test_true_3(self):
        self.assertTrue(substring_test('1234567', '541265'))

    def test_true_4(self):
        self.assertTrue(substring_test('Codewars is sweet!', 'is'))

    def test_true_5(self):
        self.assertTrue(substring_test('supercalifragilisticexpialidocious',
                                       'SoundOfItIsAtrocious'))

    def test_true_6(self):
        self.assertTrue(substring_test(
            'LoremipsumdolorsitametconsecteturadipiscingelitAeneannonaliquet'
            'ligulautplaceratorciSuspendissepotentiMorbivolutpatauctoripsume'
            'getaliquamPhasellusidmagnaelitNullamerostellustemporquismolesti'
            'eaornarevitaediamNullaaliquamrisusnonviverrasagittisInlaoreetul'
            'tricespretiumVestibulumegetnullatinciduntsempersemacrutrumfelis'
            'PraesentpurusarcutempusnecvariusidultricesaduiPellentesqueultri'
            'ciesjustolobortisrhoncusdignissimNuncviverraconsequatblanditUtb'
            'ibendumatlacusactristiqueAliquamimperdietnuncsempertortoreffici'
            'turviverra', 'thisisalongstringtest')
        )

    def test_false(self):
        self.assertFalse(substring_test('Something', 'Fun'))

    def test_false_2(self):
        self.assertFalse(substring_test('Something', ''))

    def test_false_3(self):
        self.assertFalse(substring_test('', 'Something'))

    def test_false_4(self):
        self.assertFalse(substring_test('test', 'lllt'))

    def test_false_5(self):
        self.assertFalse(substring_test('', ''))
