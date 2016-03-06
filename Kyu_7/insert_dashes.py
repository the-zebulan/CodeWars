ODD = {1, 3, 5, 7, 9}


def insert_dash(num):
    num = str(num)
    dex = {i for i, a in enumerate(num) if int(a) in ODD}
    return ''.join(b + '-' if {i, i + 1}.issubset(dex) else b
                   for i, b in enumerate(num))
