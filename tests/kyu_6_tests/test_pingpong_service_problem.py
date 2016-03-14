import unittest

from kyu_6.pingpong_service_problem import service


class ServiceTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(service('0:0'), 'first')

    def test_equals_2(self):
        self.assertEqual(service('0:5'), 'second')

    def test_equals_3(self):
        self.assertEqual(service('3:2'), 'second')

    def test_equals_4(self):
        self.assertEqual(service('5:5'), 'first')

    def test_equals_5(self):
        self.assertEqual(service('11:11'), 'first')

    def test_equals_6(self):
        self.assertEqual(service('14:15'), 'second')

    def test_equals_7(self):
        self.assertEqual(service('21:20'), 'first')

    def test_equals_8(self):
        self.assertEqual(service('21:22'), 'second')


if __name__ == '__main__':
    unittest.main()
