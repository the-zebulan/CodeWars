def hashify(string):
    result = {}
    string = string + string[0]
    for a in xrange(len(string) - 1):
        k, v = string[a:a + 2]
        try:
            result[k].append(v)         # dictionary value is a list
        except AttributeError:
            result[k] = [result[k], v]  # dictionary value is NOT a list
        except KeyError:
            result[k] = v               # dictionary key does NOT exist
    return result

assert hashify('123456') == \
    {'1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6': '1'}
assert hashify('11223') == {'1': ['1', '2'], '2': ['2', '3'], '3': '1'}
assert hashify('Codewars') == \
    {'C': 'o', 'o': 'd', 'd': 'e', 'e': 'w', 'w': 'a',
     'a': 'r', 'r': 's', 's': 'C'}
assert hashify('this is a string') == \
    {'t': ['h', 'r'], 'h': 'i', 'i': ['s', 's', 'n'], 's': [' ', ' ', 't'],
     ' ': ['i', 'a', 's'], 'a': ' ', 'r': 'i', 'n': 'g', 'g': 't'}
assert hashify('racecar') == \
    {'r': ['a', 'r'], 'a': ['c', 'r'], 'c': ['e', 'a'], 'e': 'c'}
assert hashify('CcCcCcCc') == \
    {'c': ['C', 'C', 'C', 'C'], 'C': ['c', 'c', 'c', 'c']}
