from itertools import cycle
def endlessString(s, start, length):
    dex = (start if length >= 0 else start + length + 1) % len(s)
    endless = cycle(s[dex:] + s[:dex])
    return ''.join(next(endless) for _ in xrange(abs(length)))
