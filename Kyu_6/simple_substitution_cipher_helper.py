from string import maketrans


class Cipher(object):
    def __init__(self, map1, map2):
        self.encoder = maketrans(map1, map2)
        self.decoder = maketrans(map2, map1)

    def encode(self, string):
        return string.translate(self.encoder)

    def decode(self, string):
        return string.translate(self.decoder)

one = "abcdefghijklmnopqrstuvwxyz"
two = "etaoinshrdlucmfwypvbgkjqxz"

cipher = Cipher(one, two)
assert cipher.encode("abc") == "eta"
assert cipher.encode("xyz") == "qxz"
assert cipher.decode("eirfg") == "aeiou"
assert cipher.decode("erlang") == "aikcfu"

two = 'tfozcivbsjhengarudlkpwqxmy'
cipher = Cipher(one, two)
assert cipher.encode('abc') == 'tfo'
assert cipher.decode('tfo') == 'abc'
assert cipher.decode('kjpphi') == 'tjuukf'
assert cipher.encode('ajqqtb') == 'tjuukf'
