import unittest

from Kyu_6.temperature_converter import convert_temp


class ConvertTemperatureTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(convert_temp(100, 'C', 'F'), 212)

    def test_equals_2(self):
        self.assertEqual(convert_temp(-30, 'De', 'K'), 393)

    def test_equals_3(self):
        self.assertEqual(convert_temp(40, 'Re', 'C'), 50)

    def test_equals_4(self):
        self.assertEqual(convert_temp(60, 'De', 'F'), 140)

    def test_equals_5(self):
        self.assertEqual(convert_temp(373.15, 'K', 'N'), 33)

    def test_equals_6(self):
        self.assertEqual(convert_temp(666, 'K', 'K'), 666)


if __name__ == '__main__':
    unittest.main()
