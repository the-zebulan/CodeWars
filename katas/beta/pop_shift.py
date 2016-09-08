def pop_shift(s):
    half, odd_len = divmod(len(s), 2)
    return [s[half + odd_len:][::-1], s[:half], s[half] if odd_len else '']
