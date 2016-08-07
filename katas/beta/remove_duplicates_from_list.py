def distinct(seq):
    result = []
    seen = set()
    for a in seq:
        if a not in seen:
            result.append(a)
            seen.add(a)
    return result
