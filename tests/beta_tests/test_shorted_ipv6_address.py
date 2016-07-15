import unittest

from katas.beta.shorten_ipv6_address import shorten


class ShortenIPv6TestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(shorten('2642:0006:0006:0000:0000:0000:0000:9147'),
                         '2642:6:6::9147')

    def test_equal_2(self):
        self.assertEqual(shorten('1234:0000:5678:0000:0000:90AB:0000:CDEF'),
                         '1234:0:5678::90AB:0:CDEF')

    def test_equal_3(self):
        self.assertEqual(shorten('1111:0000:0000:2222:0000:0000:3333:4444'),
                         '1111::2222:0:0:3333:4444')

    def test_equal_4(self):
        self.assertEqual(shorten('A43B:1CF6:541C:98AA:CC43:1092:E932:90AD'),
                         'A43B:1CF6:541C:98AA:CC43:1092:E932:90AD')

    def test_equal_5(self):
        self.assertEqual(shorten('9000:B004:C13A:594C:19CD:102D:394F:FCD1'),
                         '9000:B004:C13A:594C:19CD:102D:394F:FCD1')

    def test_equal_6(self):
        self.assertEqual(shorten('043B:00F6:541C:08AA:0003:1092:000D:90AD'),
                         '43B:F6:541C:8AA:3:1092:D:90AD')

    def test_equal_7(self):
        self.assertEqual(shorten('9000:0004:000A:094C:00CD:102D:394F:0001'),
                         '9000:4:A:94C:CD:102D:394F:1')

    def test_equal_8(self):
        self.assertEqual(shorten('3BDF:000E:0004:0ECD:0000:0009:3C7F:734F'),
                         '3BDF:E:4:ECD::9:3C7F:734F')

    def test_equal_9(self):
        self.assertEqual(shorten('0388:0B7B:004D:0000:00D3:FDC1:E0E8:08D7'),
                         '388:B7B:4D::D3:FDC1:E0E8:8D7')

    def test_equal_10(self):
        self.assertEqual(shorten('0018:000A:0F0C:10B2:668D:0000:0000:009B'),
                         '18:A:F0C:10B2:668D::9B')

    def test_equal_11(self):
        self.assertEqual(shorten('00AF:0000:0000:0000:0000:704E:EC20:3DAA'),
                         'AF::704E:EC20:3DAA')

    def test_equal_12(self):
        self.assertEqual(shorten('A2A5:03DB:0000:60A5:0000:0005:BD22:0000'),
                         'A2A5:3DB::60A5:0:5:BD22:0')

    def test_equal_13(self):
        self.assertEqual(shorten('0000:0FBA:0000:0000:0000:0000:057E:AFFD'),
                         '0:FBA::57E:AFFD')

    def test_equal_14(self):
        self.assertEqual(shorten('0000:0000:0000:0000:0000:0C30:00DA:29CB'),
                         '::C30:DA:29CB')

    def test_equal_15(self):
        self.assertEqual(shorten('97CA:4C84:B62B:C3A8:00F4:0000:0000:0000'),
                         '97CA:4C84:B62B:C3A8:F4::')

    def test_equal_16(self):
        self.assertEqual(shorten('0000:0391:F08E:0F28:0000:0003:0037:0006'),
                         '::391:F08E:F28:0:3:37:6')

    def test_equal_17(self):
        self.assertEqual(shorten('00C8:0000:0243:0050:ED26:008F:0000:0000'),
                         'C8:0:243:50:ED26:8F::')

    def test_equal_18(self):
        self.assertEqual(shorten('0000:0000:0001:0007:0F63:0000:4FF7:0000'),
                         '::1:7:F63:0:4FF7:0')

    def test_equal_19(self):
        self.assertEqual(shorten('0000:0000:6B6F:63B3:0000:0001:0000:0000'),
                         '::6B6F:63B3:0:1:0:0')
