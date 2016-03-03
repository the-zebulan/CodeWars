from string import maketrans


def unique_key(key):
    seen = set()
    uniq = []
    for k in key:
        if k not in seen:
            uniq.append(k)
            seen.add(k)
    return ''.join(uniq)


class keyword_cipher(object):
    """ KeywordCipher == PEP8 (forced snake_case by CodeWars) """
    def __init__(self, abc, keyword):
        key = unique_key(keyword)
        az = '{}{}'.format(key, ''.join(a for a in abc if a not in key))
        self.decode_trans = maketrans(az, abc)
        self.encode_trans = maketrans(abc, az)

    def encode(self, s):
        return s.translate(self.encode_trans)

    def decode(self, s):
        return s.translate(self.decode_trans)


cipher = keyword_cipher("abcdefghijklmnopqrstuvwxyz", "keyword")
assert cipher.encode("abc") == "key"
assert cipher.encode("xyz") == "vxz"
assert cipher.decode("key") == "abc"
assert cipher.decode("vxz") == "xyz"
