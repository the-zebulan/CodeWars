import unittest

from Kyu_6.dubstep import song_decoder


class SongDecoderTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(song_decoder('AWUBBWUBC'), 'A B C')

    def test_equals_2(self):
        self.assertEqual(song_decoder('AWUBWUBWUBBWUBWUBWUBC'), 'A B C')

    def test_equals_3(self):
        self.assertEqual(song_decoder('WUBAWUBBWUBCWUB'), 'A B C')


if __name__ == '__main__':
    unittest.main()
