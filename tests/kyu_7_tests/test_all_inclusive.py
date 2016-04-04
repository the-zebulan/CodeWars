import unittest

from katas.kyu_7.all_inclusive import contain_all_rots


class RotationsTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(contain_all_rots('bsjq', ['bsjq', 'qbsj', 'sjqb', 'twZNsslC', 'jqbs']))

    def test_true_2(self):
        self.assertTrue(contain_all_rots('', []))

    def test_true_3(self):
        self.assertTrue(contain_all_rots('', ['bsjq', 'qbsj']))

    def test_false(self):
        self.assertFalse(contain_all_rots('Ajylvpy', ['Ajylvpy', 'ylvpyAj', 'jylvpyA', 'lvpyAjy', 'pyAjylv', 'vpyAjyl', 'ipywee']))

    def test_false_2(self):
        self.assertFalse(contain_all_rots('XjYABhR', ['TzYxlgfnhf', 'yqVAuoLjMLy', 'BhRXjYA', 'YABhRXj', 'hRXjYAB', 'jYABhRX', 'XjYABhR', 'ABhRXjY']))


if __name__ == '__main__':
    unittest.main()
