import unittest

from Kyu_5.readability_is_king import flesch_kincaid


class FleschKincaidTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(flesch_kincaid('The turtle is leaving.'), 3.67)

    def test_equals_2(self):
        self.assertEqual(flesch_kincaid('A good book is hard to find.'), -1.06)

    def test_equals_3(self):
        self.assertEqual(flesch_kincaid(
            'To be or not to be. That is the question.'), -0.66)

    def test_equals_4(self):
        self.assertEqual(flesch_kincaid(
            'Do not cut your fingers as your katana is getting sharper! Be g'
            'entle.'), 4.19)

    def test_equals_5(self):
        self.assertEqual(flesch_kincaid(
            'Jumps hyperactive sweet sweet happy rests purrs jumps armchair?'
            ' Sleeps sleeps food hyperactive cuddles armchair walks rests so'
            'ft? Sleeps soft cover rests cat sun fun.'), 10.68)


if __name__ == '__main__':
    unittest.main()
