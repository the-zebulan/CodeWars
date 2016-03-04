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
