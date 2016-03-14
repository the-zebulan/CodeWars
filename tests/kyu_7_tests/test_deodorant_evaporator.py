import unittest

from katas.kyu_7.deodorant_evaporator import evaporator


class EvaporatorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(evaporator(10, 10, 10), 22)


if __name__ == '__main__':
    unittest.main()
