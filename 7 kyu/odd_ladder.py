pattern = lambda n: '\n'.join(str(a) * a for a in range(1, n + 1, 2))

assert pattern(4) == '1\n333'
assert pattern(1) == '1'
assert pattern(5) == '1\n333\n55555'
