import unittest

from kyu_6.function_iteration import create_iterator


class CreateIteratorTestCase(unittest.TestCase):
    def setUp(self):
        self.double_iterator = create_iterator(lambda a: a * 2, 1)
        self.get_quadruple = create_iterator(lambda b: b * 2, 2)

    def test_equals(self):
        self.assertEqual(self.double_iterator(3), 6)

    def test_equals_2(self):
        self.assertEqual(self.double_iterator(5), 10)

    def test_equals_3(self):
        self.assertEqual(self.get_quadruple(2), 8)

    def test_equals_4(self):
        self.assertEqual(self.get_quadruple(5), 20)


if __name__ == '__main__':
    unittest.main()
