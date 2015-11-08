from math import ceil
from string import ascii_lowercase as low, ascii_uppercase as up


def shifty(string, shift, encode=True):
    if not encode:
        string = ''.join(string)
    shifted_chars = []
    for i, a in enumerate(string, 1):
        shifter = shift if encode else -shift
        if a.islower():
            shifted_chars.append(low[(low.index(a) + shifter) % 26])
        elif a.isupper():
            shifted_chars.append(up[(up.index(a) + shifter) % 26])
        else:
            shifted_chars.append(a)
        shift += 1
    else:
        length = i
    if not encode:
        return ''.join(shifted_chars)
    chunk = int(ceil(length / 5.0))
    result = []
    for i, b in enumerate(xrange(0, length, chunk), 1):
        result.append(''.join(shifted_chars[b:b + chunk]))
    else:
        if i < 5:
            result.append('')
    return result


def demoving_shift(strings, shift):
    return shifty(strings, shift, encode=False)


def moving_shift(string, shift):
    return shifty(string, shift)


assert demoving_shift(['J vltasl rlhr ', 'zdfog odxr ypw', ' atasl rlhr p ',
                       'gwkzzyq zntyhv', ' lvz wp!!!'], 1) \
    == 'I should have known that you would have a perfect answer for me!!!'

assert moving_shift('I should have known that you would have a perfect '
                    'answer for me!!!', 1) \
    == ['J vltasl rlhr ', 'zdfog odxr ypw', ' atasl rlhr p ',
        'gwkzzyq zntyhv', ' lvz wp!!!']
