import unittest

from katas.kyu_6.binding_within_the_list_monad import bind


class BindTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(bind([1, 2, 3], lambda a: [a]), [1, 2, 3])

    def test_equals_2(self):
        self.assertEqual(bind([7, 8, 9], lambda a: [[a]]), [[7], [8], [9]])

    def test_equals_3(self):
        self.assertEqual(bind([3, 4, 5],
                              lambda a: [[a, -a]]), [[3, -3], [4, -4], [5, -5]])

    def test_equals_4(self):
        self.assertEqual(bind([5, 6, 7], lambda a: [str(a)]), ['5', '6', '7'])

    def test_equals_5(self):
        self.assertEqual(bind([1, 2, 3], lambda a: [a + 1]), [2, 3, 4])


if __name__ == '__main__':
    unittest.main()
