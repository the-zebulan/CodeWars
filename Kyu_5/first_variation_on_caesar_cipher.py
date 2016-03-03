from math import ceil
from string import ascii_lowercase as low, ascii_uppercase as up


def shifty(string, shift, encode=True):
    if not encode:
        string = ''.join(string)
    length = 0
    shifted_chars = []
    for a in string:
        shifter = shift if encode else -shift
        if a.islower():
            shifted_chars.append(low[(low.index(a) + shifter) % 26])
        elif a.isupper():
            shifted_chars.append(up[(up.index(a) + shifter) % 26])
        else:
            shifted_chars.append(a)
        length += 1
        shift += 1
    if not encode:
        return ''.join(shifted_chars)
    chunk = int(ceil(length / 5.0))
    result = [''.join(shifted_chars[b:b + chunk])
              for b in xrange(0, length, chunk)]
    return result if len(result) == 5 else result + ['']


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
