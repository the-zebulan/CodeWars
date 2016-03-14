# def in_array(array1, array2):
#     array2 = ' '.join(array2)
#     return sorted(set(a for a in array1 if a in array2))


def in_array(array1, array2):
    result = set()
    for a in array1:
        for b in array2:
            if a in b:
                result.add(a)
                break
    return sorted(result)
