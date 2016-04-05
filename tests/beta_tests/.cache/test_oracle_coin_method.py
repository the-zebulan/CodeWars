import unittest

from katas.beta.oracle_coin_method import oracle


class OracleTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(oracle([
            ['two', 'h', 'h', 't'], ['six', 't', 'h', 't'],
            ['four', 't', 't', 't'], ['one', 'h', 't', 'h'],
            ['three', 'h', 'h', 'h'], ['five', 't', 't', 'h']]),
            '---------\n---------\n----x----\n----o----\n---- ----\n---- ----'
        )

    def test_equals_2(self):
        self.assertEqual(oracle([
            ['six', 't', 't', 'h'], ['one', 'h', 'h', 't'],
            ['three', 't', 'h', 'h'], ['two', 't', 't', 't'],
            ['five', 'h', 'h', 't'], ['four', 't', 't', 'h']]),
            '---------\n---- ----\n---------\n---- ----\n----x----\n---- ----'
        )

    def test_equals_3(self):
        self.assertEqual(oracle([
            ['five', 'h', 'h', 'h'], ['four', 't', 't', 'h'],
            ['two', 'h', 't', 'h'], ['one', 'h', 'h', 't'],
            ['six', 't', 'h', 't'], ['three', 'h', 'h', 'h']]),
            '---------\n----o----\n---------\n----o----\n---- ----\n---- ----'
        )

    def test_equals_4(self):
        self.assertEqual(oracle([
            ['one', 't', 't', 't'], ['two', 't', 't', 't'],
            ['three', 'h', 't', 'h'], ['four', 'h', 'h', 't'],
            ['six', 't', 'h', 't'], ['five', 't', 'h', 'h']]),
            '---------\n---- ----\n---- ----\n---- ----\n----x----\n----x----'
        )

    def test_equals_5(self):
        self.assertEqual(oracle([
            ['three', 'h', 't', 'h'], ['four', 't', 't', 'h'],
            ['one', 'h', 'h', 'h'], ['two', 't', 't', 'h'],
            ['six', 't', 'h', 't'], ['five', 'h', 't', 'h']]),
            '---------\n---- ----\n---------\n---- ----\n---------\n----o----'
        )

    def test_equals_6(self):
        self.assertEqual(oracle([
            ['four', 't', 'h', 'h'], ['six', 't', 't', 't'],
            ['one', 'h', 'h', 't'], ['three', 't', 't', 't'],
            ['two', 't', 'h', 't'], ['five', 't', 'h', 't']]),
            '----x----\n---------\n---- ----\n----x----\n---------\n---- ----'
        )

    def test_equals_7(self):
        self.assertEqual(oracle([
            ['five', 't', 'h', 'h'], ['six', 't', 't', 't'],
            ['three', 'h', 'h', 't'], ['one', 't', 't', 't'],
            ['two', 't', 'h', 't'], ['four', 't', 'h', 't']]),
            '----x----\n---- ----\n---------\n---- ----\n---------\n----x----'
        )

    def test_equals_8(self):
        self.assertEqual(oracle([
            ['six', 't', 'h', 't'], ['one', 't', 't', 't'],
            ['four', 'h', 'h', 't'], ['three', 't', 't', 't'],
            ['two', 't', 'h', 't'], ['five', 't', 'h', 't']]),
            '---------\n---------\n---- ----\n----x----\n---------\n----x----'
        )

    def test_equals_9(self):
        self.assertEqual(oracle([
            ['two', 't', 'h', 'h'], ['six', 't', 't', 't'],
            ['one', 'h', 'h', 't'], ['three', 't', 'h', 't'],
            ['four', 't', 'h', 't'], ['five', 't', 'h', 'h']]),
            '----x----\n---- ----\n---------\n---------\n---- ----\n---- ----'
        )

    def test_equals_10(self):
        self.assertEqual(oracle([
            ['four', 't', 'h', 'h'], ['two', 't', 't', 'h'],
            ['three', 'h', 'h', 't'], ['one', 't', 'h', 'h'],
            ['five', 't', 'h', 't'], ['six', 't', 'h', 't']]),
            '---------\n---------\n---- ----\n---- ----\n---------\n---- ----'
        )


if __name__ == '__main__':
    unittest.main()
