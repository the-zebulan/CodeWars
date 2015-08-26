def arr2bin(arr):
    total = 0
    for a in arr:
        if not type(a) == int:
            return False
        total += a
    return '{:b}'.format(total)

assert arr2bin([1, 2]) == '11'
assert arr2bin([1, 2, 'a']) is False
assert arr2bin([1, 2, 3, 4, 5]) == "1111"
assert arr2bin([1, 10, 100, 1000]) == "10001010111"
assert arr2bin([94, 23, 73, True, 61]) is False
