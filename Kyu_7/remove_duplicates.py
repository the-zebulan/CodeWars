def unique(integers):
    uniq = set()
    result = []
    for a in integers:
        if a not in uniq:
            result.append(a)
        uniq.add(a)
    return result
