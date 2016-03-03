from string import ascii_uppercase as az, maketrans


class CaesarCipher(object):
    def __init__(self, shift):
        self.shifted = az[shift:] + az[:shift]
        self.decode_trans = maketrans(self.shifted, az)
        self.encode_trans = maketrans(az, self.shifted)

    def decode(self, s):
        return s.upper().translate(self.decode_trans)

    def encode(self, s):
        return s.upper().translate(self.encode_trans)


c = CaesarCipher(5)
assert c.encode('Codewars') == 'HTIJBFWX'
assert c.decode('BFKKQJX') == 'WAFFLES'
