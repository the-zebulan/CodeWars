def duplicates(array):
    seen_before = set()
    result = []
    for a in array:
        if a not in result and a in seen_before:
            result.append(a)
        seen_before.add(a)
    return result
