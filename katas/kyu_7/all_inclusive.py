# def contain_all_rots(strng, arr):
#     length = len(strng)
#     s2 = strng * 2
#     return set(s2[a:a + length] for a in xrange(length)).issubset(arr)


def contain_all_rots(strng, arr):
    return all(strng[i:] + strng[:i] in arr for i in xrange(len(strng)))
