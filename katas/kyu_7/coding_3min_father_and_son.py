def sc(strng):
    seen = set(strng)
    return ''.join(a for a in strng if a.swapcase() in seen)
