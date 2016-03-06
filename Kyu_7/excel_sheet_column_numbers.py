def title_to_number(title):
    return sum((ord(a) - 64) * (26 ** i) for i, a in enumerate(title[::-1]))
