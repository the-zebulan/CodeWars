def digital_root(n):
    return n if n <= 10 else digital_root(sum(map(int, str(n))))

assert digital_root(16) == 7
assert digital_root(942) == 6
assert digital_root(132189) == 6
assert digital_root(493193) == 2
