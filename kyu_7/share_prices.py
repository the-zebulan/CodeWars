def share_price(invested, changes):
    return '{:.2f}'.format(
        reduce(lambda a, b: a + (a * (b / 100.0)), changes, invested))
