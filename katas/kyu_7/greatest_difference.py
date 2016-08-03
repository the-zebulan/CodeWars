from re import match


def diff(pairs):
    max_diff = max_pair = False
    for pair in pairs:
        a, b = (int(c) for c in match(r'(-?\d+)-(-?\d+)$', pair).groups())
        current = abs(a - b)
        if current > max_diff:
            max_diff = current
            max_pair = pair
    return max_pair
