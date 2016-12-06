def reverse_and_mirror(s1, s2):
    swap = s1.swapcase()
    return '{}@@@{}{}'.format(s2[::-1].swapcase(), swap[::-1], swap)


# PEP8: function name should use snake_case
reverseAndMirror = reverse_and_mirror
