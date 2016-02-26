def lstzip(a, b, fn):
    return [fn(*c) for c in zip(a, b)]


a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']
assert lstzip(a, b, lambda a, b: str(a) + str(b)) == \
    ['1a', '2b', '3c', '4d', '5e']
assert lstzip(b, a, lambda a, b: str(a) + str(b)) == \
    ['a1', 'b2', 'c3', 'd4', 'e5']
assert lstzip(b, lstzip(a, b, lambda a, b: a * ord(b[0])),
              lambda a, b: str(a) + str(b)) == \
    ['a97', 'b196', 'c297', 'd400', 'e505']
