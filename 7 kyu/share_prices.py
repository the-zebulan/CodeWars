def share_price(invested, changes):
    return '{:.2f}'.format(
        reduce(lambda a, b: a + (a * (b / 100.0)), changes, invested))

assert share_price(100, []) == '100.00'
assert share_price(100, [-50, 50]) == '75.00'
assert share_price(100, [-50, 100]) == '100.00'
assert share_price(100, [-20, 30]) == '104.00'
assert share_price(1000, [0, 2, 3, 6]) == '1113.64'
