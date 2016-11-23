def to_nums(s):
    result = [int(a) for a in s.split('.')]
    while True:
        try:
            if result[-1] != 0:
                break
        except IndexError:
            return [0]
        result.pop()
    return result


def compare(s1, s2):
    a = to_nums(s1)
    b = to_nums(s2)
    return (a > b) - (a < b)
