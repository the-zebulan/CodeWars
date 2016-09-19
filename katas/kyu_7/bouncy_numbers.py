def is_bouncy(n):
    s = str(n)
    decrease = increase = False
    for a, b in zip(s, s[1:]):
        if a < b:
            increase = True
        elif a > b:
            decrease = True
    return decrease and increase
