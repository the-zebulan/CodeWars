from string import ascii_lowercase as az, digits

VALID = set(az + digits + '?$. ')


def general(s):
    return ' '.join(
            ''.join(w[i:i + 2][::-1] for i in xrange(0, len(w), 2)) for w in
            ''.join(a for a in s.lower() if a in VALID).split())


assert general("etts noe si a usccses") == "test one is a success"
assert general("1$2.3") == "$1.23"
