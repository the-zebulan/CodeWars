import unittest

from Beta.count_words import word_count


class WordCountTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(word_count(
            'Hello there, little user5453 374 ())$.'), 4)

    def test_equals_2(self):
        self.assertEqual(word_count('hello there'), 2)

    def test_equals_3(self):
        self.assertEqual(word_count('hello there and hi'), 4)

    def test_equals_4(self):
        self.assertEqual(word_count(
            'Really2374239847 long ^&#$&(*@# sequence'), 3)

    def test_equals_5(self):
        self.assertEqual(word_count(
            'I\'d been using my sphere as a stool. I traced counterclockwise'
            ' circles on it with my fingertips and it shrank until I could '
            'palm it. My bolt had shifted while I\'d been sitting. I pulled '
            'it up and yanked the pleats straight as I careered around '
            'tables, chairs, globes, and slow-moving fraas. I passed under '
            'a stone arch into the Scriptorium. The place smelled richly of'
            ' ink. Maybe it was because an ancient fraa and his two fids '
            'were copying out books there. But I wondered how long it would'
            ' take to stop smelling that way if no one ever used it at all;'
            ' a lot of ink had been spent there, and the wet smell of it '
            'must be deep into everything.'), 112)


if __name__ == '__main__':
    unittest.main()
