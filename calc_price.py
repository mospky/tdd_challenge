import math

class Calc:
    def calc_price(self, moneys):
        """受け取ったお金に消費税をかける"""
        total = 0
        for money_i in moneys:
            total += round(money_i * 1.1)

        return total


    def round(self, flo):
        """少数を丸めます"""
        return math.floor(flo+0.5)

if __name__ == "__main__":
    calc = Calc()
    result = calc.calc_price([10, 12])
    print(result)
    result = calc.calc_price([40, 16])
    print(result)
    result = calc.calc_price([100, 45])
    print(result)
    result = calc.calc_price([50, 50, 55])
    print(result)
    result = calc.calc_price([1000])
    print(result)
    result = calc.calc_price([20, 40])
    print(result)
    result = calc.calc_price([30, 60, 90])
    print(result)
    result = calc.calc_price([11, 12, 13])
    print(result)