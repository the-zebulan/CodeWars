import unittest

from katas.kyu_5.valid_date_regex import valid_date


class ValidDateTestCase(unittest.TestCase):
    def test_none(self):
        self.assertIsNone(valid_date.search("[02-31]"))

    def test_none_2(self):
        self.assertIsNone(valid_date.search("[ 6-03]"))

    def test_none_3(self):
        self.assertIsNone(valid_date.search("[02-00]"))

    def test_none_4(self):
        self.assertIsNone(valid_date.search("[13-02]"))

    def test_not_none(self):
        self.assertIsNotNone(valid_date.search("[01-23]"))

    def test_not_none_2(self):
        self.assertIsNotNone(valid_date.search("[02-16]"))

    def test_not_none_3(self):
        self.assertIsNotNone(valid_date.search("ignored [08-11] ignored"))

    def test_not_none_4(self):
        self.assertIsNotNone(valid_date.search("[3] [12-04] [09-tenth]"))

    def test_not_none_5(self):
        self.assertIsNotNone(valid_date.search("[[[08-29]]]"))

    def test_not_none_6(self):
        self.assertIsNotNone(valid_date.search("[02-[08-11]04]"))


if __name__ == '__main__':
    unittest.main()
