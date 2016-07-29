def string_cnt(s):
    try:
        return s.isalpha() and sum(ord(a) for a in s.upper())
    except AttributeError:
        return 0


def compare(s1, s2):
    return string_cnt(s1) == string_cnt(s2)
