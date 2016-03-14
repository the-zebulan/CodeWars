def accum(s):
    return '-'.join(str.title(a * i) for i, a in enumerate(s, 1))
