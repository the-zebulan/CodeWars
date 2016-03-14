import unittest

from katas.beta.addition_function_problem import add


class AdditionTestCase(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(add(1, 3), 4)

    def test_equal_2(self):
        self.assertEqual(add(2, 4), 6)


if __name__ == '__main__':
    unittest.main()
