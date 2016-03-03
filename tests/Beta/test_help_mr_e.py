import unittest

from Beta.help_mr_e import evenator


class EvenatorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(evenator('How did we end up here? We go?'),
                         'Howw didd we endd up here We go')

    def test_equals_2(self):
        self.assertEqual(evenator('I got a hole in 1!'),
                         'II gott aa hole in 11')


if __name__ == '__main__':
    unittest.main()
