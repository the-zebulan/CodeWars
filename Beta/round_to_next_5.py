def round_to_next5(n):
    # return (n + 4) / 5 * 5
    q, r = divmod(n, 5)
    return n if not r else (q + 1) * 5

assert round_to_next5(0) == 0
assert round_to_next5(1) == 5
assert round_to_next5(5) == 5
assert round_to_next5(7) == 10
assert round_to_next5(20) == 20
assert round_to_next5(39) == 40
