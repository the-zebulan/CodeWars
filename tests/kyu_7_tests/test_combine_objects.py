import unittest

from katas.kyu_7.combine_objects import combine


class CombineObjectsTestCase(unittest.TestCase):
    def setUp(self):
        self.a = {'a': 10, 'b': 20, 'c': 30}
        self.b = {'a': 3, 'c': 6, 'd': 3}
        self.c = {'a': 5, 'd': 11, 'e': 8}
        self.d = {'c': 3}

    def test_equals(self):
        self.assertEqual(combine(self.a, self.b),
                         {'a': 13, 'b': 20, 'c': 36, 'd': 3})

    def test_equals_2(self):
        self.assertEqual(combine(self.a, self.c),
                         {'a': 15, 'b': 20, 'c': 30, 'd': 11, 'e': 8})

    def test_equals_3(self):
        self.assertEqual(combine(self.a, self.b, self.c),
                         {'a': 18, 'b': 20, 'c': 36, 'd': 14, 'e': 8})

    def test_equals_4(self):
        self.assertEqual(combine(self.a, self.c, self.d),
                         {'a': 15, 'b': 20, 'c': 33, 'd': 11, 'e': 8})

    def test_equals_5(self):
        self.assertEqual(combine({}, {}, {}), {})

    def test_equals_6(self):
        self.assertEqual(combine(self.a, self.c, {}),
                         {'a': 15, 'b': 20, 'c': 30, 'd': 11, 'e': 8})

    def test_equals_7(self):
        self.assertEqual(combine({}), {})

    def test_equals_8(self):
        self.assertEqual(combine(self.a, self.a, self.a),
                         {'a': 30, 'b': 60, 'c': 90})

    def test_equals_9(self):
        self.assertEqual(combine(
            self.d, self.d, self.d, self.d, self.d, self.d
        ), {'c': 18})

    def test_equals_10(self):
        self.assertEqual(combine(self.a, {}, self.a),
                         {'a': 20, 'b': 40, 'c': 60})
