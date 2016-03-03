def adjust(coin, price):
    q, r = divmod(price, coin)
    return price if not r else (q + 1) * coin

assert adjust(3, 0) == 0
assert adjust(3, 1) == 3
assert adjust(3, -2) == 0
assert adjust(3, -4) == -3
assert adjust(3, 3) == 3
assert adjust(3, 6) == 6
assert adjust(3, 7) == 9
