from string import maketrans


class Cipher(object):
    def __init__(self, map1, map2):
        self.encoder = maketrans(map1, map2)
        self.decoder = maketrans(map2, map1)

    def encode(self, string):
        return string.translate(self.encoder)

    def decode(self, string):
        return string.translate(self.decoder)
