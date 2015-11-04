def calculate(a, o, b):
    try:
        if o in '+-*/':
            return eval('{}{}{}'.format(a, o, b))
    except (SyntaxError, ZeroDivisionError):
        return None

assert calculate(6, "-", 1.5) == 4.5
assert calculate(-4, "*", 8) == -32
assert calculate(49, "/", -7) == -7
assert calculate(8, "m", 2) is None
assert calculate(4, "/", 0) is None
