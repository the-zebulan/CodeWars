def get_middle(s):
    q, r = divmod(len(s), 2)
    return s[q - (1 if not r else 0):q + 1]
