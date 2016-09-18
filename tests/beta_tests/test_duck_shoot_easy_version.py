import unittest

from katas.beta.duck_shoot_easy_version import duck_shoot


class DuckShootTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(duck_shoot(4, 0.64, '|~~2~~~22~2~~22~2~~~~2~~~|'),
                         '|~~X~~~X2~2~~22~2~~~~2~~~|')

    def test_equal_2(self):
        self.assertEqual(duck_shoot(9, 0.22, '|~~~~~~~2~2~~~|'),
                         '|~~~~~~~X~2~~~|')

    def test_equal_3(self):
        self.assertEqual(duck_shoot(6, 0.41, '|~~~~~22~2~~~~~|'),
                         '|~~~~~XX~2~~~~~|')

    def test_equal_4(self):
        self.assertEqual(duck_shoot(8, 0.05, '|2~~~~|'), '|2~~~~|')

    def test_equal_5(self):
        self.assertEqual(duck_shoot(8, 0.92, '|~~~~2~2~~~~~22~~2~~~~2~~~2|'),
                         '|~~~~X~X~~~~~XX~~X~~~~X~~~X|')
