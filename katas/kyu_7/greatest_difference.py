def diff(pairs):
    max_diff = max_pair = False
    for pair in pairs:
        a, _, b = pair.partition('-')
        current = abs(int(a) - int(b))
        if current > max_diff:
            max_diff = current
            max_pair = pair
    return max_pair
