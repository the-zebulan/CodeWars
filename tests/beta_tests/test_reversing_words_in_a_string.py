import unittest

from katas.beta.reversing_words_in_a_string import reverse


class ReverseWordsInAStringTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(reverse('Hello World'), 'World Hello')

    def test_equal_2(self):
        self.assertEqual(reverse('Hi There.'), 'There. Hi')

    def test_equal_3(self):
        self.assertEqual(reverse(
            'hlltqtwwurrfpuffha kawtffosefiagsfsyeqs rle udpywpfghy  '
        ), '  udpywpfghy rle kawtffosefiagsfsyeqs hlltqtwwurrfpuffha')

    def test_equal_4(self):
        self.assertEqual(reverse(' gdgtqgi ihwofkpshesuurawe gtgr  '),
                         '  gtgr ihwofkpshesuurawe gdgtqgi ')
