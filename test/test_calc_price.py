from tdd_challenge.calc_price import Calc
import unittest


class TestCase(unittest.TestCase):
    """消費税"""
    def test_calc_price(self):
        """税込みにします"""
        calc = Calc()
        self.assertEqual(calc.calc_price([100]), 110, "100*1.10== 110")
        self.assertEqual(calc.calc_price([100, 100]), 220, "100*1.10 + 100*1.10== 110")
        self.assertEqual(calc.calc_price([100, 45]), 160, "160")
        self.assertEqual(calc.calc_price([1000000, 1000000]),2200000, "0")



    def test_round(self):
        """少数を丸めます"""
        calc = Calc()
        self.assertEqual(calc.round(2.1), 2, "2.1 == 2")
        self.assertEqual(calc.round(2.5), 3, "2.5 == 3")





