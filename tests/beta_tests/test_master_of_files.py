import unittest

from katas.beta.master_of_files import is_audio, is_img


class MasterOfFilesTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(is_audio("NothingElseMatters.mp3"))

    def test_true_2(self):
        self.assertTrue(is_audio("DaftPunk.flac"))

    def test_true_3(self):
        self.assertTrue(is_audio("AmonTobin.aac"))

    def test_true_4(self):
        self.assertTrue(is_audio("tobin.alac"))

    def test_true_5(self):
        self.assertTrue(is_img("Home.jpg"))

    def test_true_6(self):
        self.assertTrue(is_img("flat.jpeg"))

    def test_true_7(self):
        self.assertTrue(is_img("icon.bmp"))

    def test_true_8(self):
        self.assertTrue(is_img("bounce.gif"))

    def test_true_9(self):
        self.assertTrue(is_img("transparency.png"))

    def test_false_1(self):
        self.assertFalse(is_audio("Nothing Else Matters.mp3"))

    def test_false_2(self):
        self.assertFalse(is_audio("DaftPunk.FLAC"))

    def test_false_3(self):
        self.assertFalse(is_audio(" Amon Tobin.alac"))

    def test_false_4(self):
        self.assertFalse(is_img("icon2.jpg"))

    def test_false_5(self):
        self.assertFalse(is_img("animate bounce.GIF"))
