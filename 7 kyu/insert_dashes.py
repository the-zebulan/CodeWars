ODD = {1, 3, 5, 7, 9}


def insert_dash(num):
    num = str(num)
    dex = {i for i, a in enumerate(num) if int(a) in ODD}
    return ''.join(b + '-' if {i, i + 1}.issubset(dex) else b
                   for i, b in enumerate(num))

assert insert_dash(454793) == '4547-9-3'
assert insert_dash(123456) == '123456'
assert insert_dash(1003567) == '1003-567'
assert insert_dash(24680) == '24680'
assert insert_dash(13579) == '1-3-5-7-9'
