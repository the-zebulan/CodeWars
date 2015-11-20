def rgb_range(n):
    return min(255, max(n, 0))


def rgb(r, g, b):
    return ('{:02X}' * 3).format(rgb_range(r), rgb_range(g), rgb_range(b))


assert rgb(0, 0, 0) == '000000'
assert rgb(1, 2, 3), '010203'
assert rgb(-20, 275, 125), '00FF7D'
assert rgb(148, 0, 211) == '9400D3'
assert rgb(254, 253, 252), 'FEFDFC'
assert rgb(255, 255, 255) == 'FFFFFF'
assert rgb(255, 255, 300) == 'FFFFFF'
