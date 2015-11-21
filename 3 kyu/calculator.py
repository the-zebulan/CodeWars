class Calculator(object):
    @staticmethod
    def evaluate(string):
        return round(eval(string), 3)


assert Calculator().evaluate('2 / 2 + 3 * 4 - 6') == 7
