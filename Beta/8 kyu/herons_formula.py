def heron(a, b, c):
    """ https://en.wikipedia.org/wiki/Heron%27s_formula """
    s = (a + b + c) / 2.0
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

assert heron(4, 13, 15) == 24
assert heron(4, 3, 5) == 6
assert heron(17, 25, 26) == 204
