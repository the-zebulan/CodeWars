def is_rotation(s1, s2):
    return s1 in s2 + s2 and len(s1) == len(s2)


assert is_rotation('hello', 'ohell') is True
assert is_rotation('hello', 'elloh') is True
assert is_rotation('hello', 'lloeh') is False
assert is_rotation('hello', 'hellohello') is False
