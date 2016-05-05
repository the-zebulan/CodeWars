def unite_unique(*args):
    result = []
    for a in args:
        for b in a:
            if b not in result:
                result.append(b)
    return result
