def comp(array1, array2):
    if None in (array1, array2):
        return False
    return sorted(a ** 2 for a in array1) == sorted(array2)
