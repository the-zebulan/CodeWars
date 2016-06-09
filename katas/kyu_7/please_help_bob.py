import re

VOWELS = frozenset('aeiouAEIOU')


def err_bob(s):
    result = []
    for word in re.split(r'(\s+)', s):
        for i, a in zip(xrange(len(word), -1, -1), reversed(word)):
            if a.isalpha():
                if a in VOWELS:
                    result.append(word)
                else:
                    result.append('{}{}{}'.format(
                        word[:i], 'err' if a.islower() else 'ERR', word[i:]
                    ))
                break
        else:
            result.append(word)
    return ''.join(result)
