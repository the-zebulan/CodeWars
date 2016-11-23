def to_tuple(s):
    result = [int(a) for a in s.split('.')]
    while result[-1] == 0:
        result.pop()
    return result


def compare(s1, s2):
    a = to_tuple(s1)
    b = to_tuple(s2)
    return (a > b) - (a < b)
