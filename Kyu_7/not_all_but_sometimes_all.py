def remove(text, what):
    result = []
    for a in text:
        try:
            if what[a] >= 1:
                what[a] -= 1
                continue
        except KeyError:
            pass
        result.append(a)
    return ''.join(result)
