import unittest

from katas.beta.decipher_the_cipher import encrypter


class TestDecipherTheCipher(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(encrypter("amz"), "man")

    def test_equal_2(self):
        self.assertEqual(encrypter("welcome to the organization"), "qibkyai ty tfi yvgmzenmteyz")

    def test_equal_3(self):
        self.assertEqual(encrypter("hello"), "fibby")

    def test_equal_4(self):
        self.assertEqual(encrypter("my name is"), "ao zmai eu")

    def test_equal_5(self):
        self.assertEqual(encrypter("goodbye"), "gyyjloi")


if __name__ == '__main__':
    unittest.main()
