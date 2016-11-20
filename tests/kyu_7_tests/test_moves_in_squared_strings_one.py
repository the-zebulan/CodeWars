import unittest
from textwrap import dedent

from katas.kyu_7.moves_in_squared_strings_one import (
    hor_mirror, oper, vert_mirror)


class SquaredStringsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(oper(vert_mirror, dedent('''\
            hSgdHQ
            HnDMao
            ClNNxX
            iRvxxH
            bqTVvA
            wvSyRu''')), dedent('''\
            QHdgSh
            oaMDnH
            XxNNlC
            HxxvRi
            AvVTqb
            uRySvw'''))

    def test_equal_2(self):
        self.assertEqual(oper(vert_mirror, dedent('''\
            IzOTWE
            kkbeCM
            WuzZxM
            vDddJw
            jiJyHF
            PVHfSx''')), dedent('''\
            EWTOzI
            MCebkk
            MxZzuW
            wJddDv
            FHyJij
            xSfHVP'''))

    def test_equal_3(self):
        self.assertEqual(oper(hor_mirror, dedent('''\
            lVHt
            JVhv
            CSbg
            yeCt''')), dedent('''\
            yeCt
            CSbg
            JVhv
            lVHt'''))

    def test_equal_4(self):
        self.assertEqual(oper(hor_mirror, dedent('''\
            njMK
            dbrZ
            LPKo
            cEYz''')), dedent('''\
            cEYz
            LPKo
            dbrZ
            njMK'''))
