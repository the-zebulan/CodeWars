import unittest

from katas.kyu_6.your_order_please import order


class OrderTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(order('is2 Thi1s T4est 3a'), 'Thi1s is2 3a T4est')


if __name__ == '__main__':
    unittest.main()
