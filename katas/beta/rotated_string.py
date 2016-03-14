def is_rotation(s1, s2):
    return s1 in s2 + s2 and len(s1) == len(s2)
