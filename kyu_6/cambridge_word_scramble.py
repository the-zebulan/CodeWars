from random import shuffle
from re import findall


def mix_words(s):
    result = []
    for word in findall(r"[\w']+|[ .,!?:;/-]", s):
        if len(word) > 3:
            orig = list(word[1:-1])
            mid = orig[:]
            while mid == orig:
                shuffle(mid)
            result.append('{}{}{}'.format(word[0], ''.join(mid), word[-1]))
        else:
            result.append(word)
    return ''.join(result)
