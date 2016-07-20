def string_cnt(s):
    try:
        if s.isalpha():
            return sum(ord(a) for a in s.upper())
    except AttributeError:
        pass
    return 0


def compare(s1, s2):
    return string_cnt(s1) == string_cnt(s2)
