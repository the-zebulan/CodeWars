from math import ceil
from string import ascii_lowercase as low, ascii_uppercase as up


def shifty(string, shift=None, encode=True):
    if not encode:
        string = ''.join(string)
        shift = ord(string[0]) - ord(string[1])
        string = string[2:]
        shifted_chars = []
        length = 0
    else:
        first = string[0].lower()
        shifted_chars = [first, low[(low.index(first) + shift) % 26]]
        length = 2
    for a in string:
        if a.islower():
            shifted_chars.append(low[(low.index(a) + shift) % 26])
        elif a.isupper():
            shifted_chars.append(up[(up.index(a) + shift) % 26])
        else:
            shifted_chars.append(a)
        length += 1
    if not encode:
        return ''.join(shifted_chars)
    chunk = int(ceil(length / 5.0))
    return [''.join(shifted_chars[b:b + chunk])
            for b in xrange(0, length, chunk)]


def encode_str(string, shift):
    return shifty(string, shift)


def decode(arr):
    return shifty(arr, encode=False)


u = "I should have known that you would have a perfect answer for me!!!"
v = ["ijJ tipvme ibw", "f lopxo uibu z", "pv xpvme ibwf ",
     "b qfsgfdu botx", "fs gps nf!!!"]
assert decode(v) == u
assert encode_str(u, 1) == v

u = "O CAPTAIN! my Captain! our fearful trip is done;"
v = ["opP DBQUBJ", "O! nz Dbqu", "bjo! pvs g", "fbsgvm usj", "q jt epof;"]
assert decode(v) == u
assert encode_str(u, 1) == v
