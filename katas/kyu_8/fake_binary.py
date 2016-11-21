def fake_bin(x):
    return ''.join('0' if int(a) < 5 else '1' for a in x)
