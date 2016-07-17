def flatten_me(lst):
    result = []
    for a in lst:
        try:
            result.extend(a)
        except TypeError:
            result.append(a)
    return result
