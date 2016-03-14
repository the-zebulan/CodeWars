import unittest

from katas.kyu_5.vector_class import Vector


class VectorTestCase(unittest.TestCase):
    def setUp(self):
        self.a = Vector([1, 2, 3])
        self.b = Vector([3, 4, 5])
        self.c = Vector([5, 6, 7, 8])
        self.d = Vector([1, 2])
        self.e = Vector([3, 4])

    def test_equals(self):
        self.assertEqual(self.a.dot(self.b), 26)

    def test_equals_2(self):
        self.assertEqual(self.a.norm(), 14 ** 0.5)

    def test_equals_3(self):
        self.assertEqual(str(self.a), '(1,2,3)')

    def test_true(self):
        self.assertTrue(self.a.add(self.b).equals(Vector([4, 6, 8])))

    def test_true_2(self):
        self.assertTrue(self.a.subtract(self.b).equals(Vector([-2, -2, -2])))

    def test_true_3(self):
        self.assertTrue(self.d.add(self.e).equals(Vector([4, 6])))

    def test_exception(self):
        self.assertRaises(TypeError, self.a.add, self.c)


if __name__ == '__main__':
    unittest.main()
