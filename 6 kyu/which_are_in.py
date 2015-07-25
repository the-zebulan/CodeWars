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

a1 = ['live', 'arp', 'strong']
a2 = ['lively', 'alive', 'harp', 'sharp', 'armstrong']
assert in_array(a1, a2) == ['arp', 'live', 'strong']
