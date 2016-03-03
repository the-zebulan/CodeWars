def heron(a, b, c):
    """ https://en.wikipedia.org/wiki/Heron%27s_formula """
    s = (a + b + c) / 2.0
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5
