def mygcd(a, b):
    while b:
        a, b = b, a % b
    return a

assert mygcd(30, 12) == 6
assert mygcd(8, 9) == 1
assert mygcd(1, 1) == 1
assert mygcd(74634, 73865) == 1
assert mygcd(10927782, 6902514) == 846
assert mygcd(1590771464, 1590771620) == 4
