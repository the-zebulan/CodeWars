def rgb_range(n):
    return min(255, max(n, 0))


def rgb(r, g, b):
    return ('{:02X}' * 3).format(rgb_range(r), rgb_range(g), rgb_range(b))
