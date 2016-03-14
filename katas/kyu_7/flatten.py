def flatten(lst):
    result = []
    for a in lst:
        if isinstance(a, list):
            result.extend(a)
        else:
            result.append(a)
    return result
