def remove(text, what):
    result = []
    for a in text:
        try:
            if what[a] >= 1:
                what[a] -= 1
                continue
        except KeyError:
            pass
        result.append(a)
    return ''.join(result)


assert remove('this is a string', {'t': 1, 'i': 2}) == 'hs s a string'
assert remove('hello world', {'x': 5, 'i': 2}) == 'hello world'
assert remove('apples and bananas', {'a': 50, 'n': 1}) == 'pples d bnns'
assert remove('a', {'a': 1, 'n': 1}) == ''
assert remove('codewars', {'c': 5, 'o': 1, 'd': 1, 'e': 1, 'w': 1, 'z': 1,
                           'a': 1, 'r': 1, 's': 1}) == ''
