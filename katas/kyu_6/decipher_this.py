import re

REGEX = re.compile(r'(\d+)([a-zA-Z]*)$')


def decipher_this(s):
    result = []
    for word in s.split():
        m = REGEX.match(word)
        digits, chars = m.groups()
        tmp = [chr(int(digits))]
        if len(chars) < 2:
            tmp.append(chars)
        else:
            tmp.append('{}{}{}'.format(chars[-1], chars[1:-1], chars[0]))
        result.append(''.join(tmp))
    return ' '.join(result)
