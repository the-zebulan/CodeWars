import unittest

from katas.kyu_7.make_them_bark import Dog


class DogTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(
            Dog('Apollo', 'Dobermann', 'male', '4').bark(), 'Woof!'
        )

    def test_equals_2(self):
        self.assertEqual(
            Dog('Zeus', 'Dobermann', 'male', '4').bark(), 'Woof!'
        )


if __name__ == '__main__':
    unittest.main()
