import unittest

from katas.beta.password_maker import make_password


class MakePasswordTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(
            make_password('Give me liberty or give me death'), 'Gml0gmd'
        )

    def test_equals_2(self):
        self.assertEqual(make_password('Keep Calm and Carry On'), 'KCaC0')


if __name__ == '__main__':
    unittest.main()
