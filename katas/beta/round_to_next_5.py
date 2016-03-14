def round_to_next5(n):
    # return (n + 4) / 5 * 5
    q, r = divmod(n, 5)
    return n if not r else (q + 1) * 5
