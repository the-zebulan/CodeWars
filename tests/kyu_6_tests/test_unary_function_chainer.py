import unittest

from katas.kyu_6.unary_function_chainer import chained


class ChainedTestCase(unittest.TestCase):
    def setUp(self):
        self.f1 = lambda a: a * 2
        self.f2 = lambda b: b + 2
        self.f3 = lambda c: c ** 2
        self.f4 = lambda d: d.split()
        self.f5 = lambda e: [f[::-1].title() for f in e]
        self.f6 = lambda g: '_'.join(g)

    def test_equal_1(self):
        self.assertEqual(chained([self.f1, self.f2, self.f3])(0), 4)

    def test_equal_2(self):
        self.assertEqual(chained([self.f1, self.f2, self.f3])(2), 36)

    def test_equal_3(self):
        self.assertEqual(chained([self.f3, self.f2, self.f1])(2), 12)

    def test_equal_4(self):
        self.assertEqual(
            chained([self.f4, self.f5, self.f6])('lorem ipsum dolor'),
            'Merol_Muspi_Rolod'
        )
