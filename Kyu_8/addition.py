def on_square(square):
    return pow(2, square - 1)


def total_after(square):
    return sum(pow(2, x) for x in xrange(square))
