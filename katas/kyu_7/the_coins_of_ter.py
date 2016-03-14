def adjust(coin, price):
    q, r = divmod(price, coin)
    return price if not r else (q + 1) * coin
