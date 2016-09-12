# coding=utf-8
import unittest

from katas.beta.heavy_metal_umlauts import heavy_metal_umlauts


class HeavyMetalUmlautsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(heavy_metal_umlauts(
            'Announcing the Macbook Air Guitar'
        ), 'Ännöüncïng thë Mäcböök Äïr Güïtär')

    def test_equal_2(self):
        self.assertEqual(heavy_metal_umlauts(
            'Facebook introduces new heavy metal reaction buttons'
        ), 'Fäcëböök ïntrödücës nëw hëävÿ mëtäl rëäctïön büttöns')

    def test_equal_3(self):
        self.assertEqual(heavy_metal_umlauts(
            "Strong sales of Google's VR Metalheadsets send tech stock pric"
            "es soaring"
        ), "Ströng sälës öf Gööglë's VR Mëtälhëädsëts sënd tëch stöck prïcë"
           "s söärïng")

    def test_equal_4(self):
        self.assertEqual(heavy_metal_umlauts(
            'Vegan Black Metal Chef hits the big time on Amazon TV'
        ), 'Vëgän Bläck Mëtäl Chëf hïts thë bïg tïmë ön Ämäzön TV')
