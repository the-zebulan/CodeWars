import unittest

from kyu_6.cambridge_word_scramble import mix_words


class MixWordsTestCase(unittest.TestCase):
    def setUp(self):
        self.test1 = mix_words('hello')
        self.test2 = mix_words('hello Pippi')
        self.test3 = mix_words('hello, Pippi!')

    def test_equals(self):
        self.assertEqual(len(self.test1), 5)

    def test_equals_2(self):
        self.assertEqual(self.test1[0], 'h')

    def test_equals_3(self):
        self.assertEqual(self.test1[4], 'o')

    def test_equals_4(self):
        self.assertEqual(''.join(sorted(self.test1[1:4])), 'ell')

    def test_equals_5(self):
        self.assertEqual(len(self.test2), 11)

    def test_equals_6(self):
        self.assertEqual(self.test2[0], 'h')

    def test_equals_7(self):
        self.assertEqual(self.test2[4], 'o')

    def test_equals_8(self):
        self.assertEqual(self.test2[5], ' ')

    def test_equals_9(self):
        self.assertEqual(self.test2[6], 'P')

    def test_equals_10(self):
        self.assertEqual(self.test2[10], 'i')

    def test_equals_11(self):
        self.assertEqual(''.join(sorted(self.test2[1:4])), 'ell')

    def test_equals_12(self):
        self.assertEqual(''.join(sorted(self.test2[7:10])), 'ipp')

    def test_equals_13(self):
        self.assertEqual(len(self.test3), 13)

    def test_equals_14(self):
        self.assertEqual(self.test3[0], 'h')

    def test_equals_15(self):
        self.assertEqual(self.test3[4], 'o')

    def test_equals_16(self):
        self.assertEqual(self.test3[5], ',')

    def test_equals_17(self):
        self.assertEqual(self.test3[6], ' ')

    def test_equals_18(self):
        self.assertEqual(self.test3[7], 'P')

    def test_equals_19(self):
        self.assertEqual(self.test3[11], 'i')

    def test_equals_20(self):
        self.assertEqual(self.test3[12], '!')

    def test_equals_21(self):
        self.assertEqual(''.join(sorted(self.test3[1:4])), 'ell')

    def test_equals_22(self):
        self.assertEqual(''.join(sorted(self.test3[8:11])), 'ipp')

    def test_equals_23(self):
        self.assertEqual(mix_words('Hi'), 'Hi')

    def test_equals_24(self):
        self.assertEqual(mix_words('Hi!'), 'Hi!')

    def test_equals_25(self):
        self.assertEqual(mix_words('Hey'), 'Hey')

    def test_equals_26(self):
        self.assertEqual(mix_words('Hey?'), 'Hey?')

    def test_not_equal(self):
        self.assertNotEqual(self.test1, 'hello')

    def test_not_equal_2(self):
        self.assertNotEqual(self.test2, 'hello Pippi')

    def test_not_equal_3(self):
        self.assertNotEqual(self.test3, 'hello, Pippi!')


if __name__ == '__main__':
    unittest.main()
