import unittest

from katas.kyu_7.the_owls_are_not_what_they_seem import owl_pic


class OwlTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(owl_pic('xwe'), 'XW\'\'0v0\'\'WX')

    def test_equals_2(self):
        self.assertEqual(owl_pic('kuawd6r8q27y87t93r76352475437'),
                         'UAW8Y8T\'\'0v0\'\'T8Y8WAU')

    def test_equals_3(self):
        self.assertEqual(owl_pic('t6ggggggggWw'), 'TWW\'\'0v0\'\'WWT')


if __name__ == '__main__':
    unittest.main()
