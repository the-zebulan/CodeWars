class Calculator(object):
    @staticmethod
    def evaluate(string):
        return round(eval(string), 3)
