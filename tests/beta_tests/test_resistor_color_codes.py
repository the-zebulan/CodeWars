import unittest

from katas.beta.resistor_color_codes import decode_resistor_colors


class DecodeResistorColorsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(decode_resistor_colors('yellow violet black'),
                         '47 ohms, 20%')

    def test_equal_2(self):
        self.assertEqual(decode_resistor_colors('yellow violet red gold'),
                         '4.7k ohms, 5%')

    def test_equal_3(self):
        self.assertEqual(decode_resistor_colors('brown black green silver'),
                         '1M ohms, 10%')
