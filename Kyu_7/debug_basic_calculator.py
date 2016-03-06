def calculate(a, o, b):
    try:
        if o in '+-*/':
            return eval('{}{}{}'.format(a, o, b))
    except (SyntaxError, ZeroDivisionError):
        return None
