def problem(a):
    return a * 50 + 6 if not isinstance(a, str) else 'Error'

assert problem("hello") == "Error"
assert problem(1) == 56
