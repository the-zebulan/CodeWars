# coding=utf-8
from operator import add, sub


class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.az_dex = {a: i for i, a in enumerate(alphabet)}
        # self.az_dex = {a: i for i, a in enumerate(alphabet.decode('utf-8'))}
        self.az_len = len(alphabet)
        self.key = key
        self.key_len = len(self.key)

    def encode(self, strng):
        return self.flip(strng)

    def decode(self, strng):
        return self.flip(strng, encode=False)

    def flip(self, strng, encode=True):
        result = []
        func = add if encode else sub
        for i, a in enumerate(strng):
            if a.isalpha():
                try:
                    result.append(self.alphabet[func(self.az_dex[a],
                        self.az_dex[self.key[i % self.key_len]]) % self.az_len])
                except KeyError:
                    result.append(a)
            else:
                result.append(a)
        return ''.join(result)


abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
cipher = VigenereCipher(key, abc)

print cipher.encode('codewars') == 'rovwsoiv'
print cipher.encode('srawedoc') == 'hrsoarff'
print cipher.decode('rovwsoiv') == 'codewars'
print cipher.decode('hrsoarff') == 'srawedoc'

# abc = 'アイウエオァィゥェォカキクケコサシスセソタチツッテトナニヌネノハヒフヘホマミムメモヤャユュヨョラリ'
abc = 'アイウエオァィゥェォカキクケコサシスセソタチツッテトナニヌネノハヒフヘホマミムメモヤャユュヨョラリルレロワヲンー'
key = 'カタカナ'
cipher = VigenereCipher(key, abc)
# print len(abc)
print cipher.encode('カタカナ')
# '\xe3\x82\xab \xe3\x82\xbf \xe3\x82\xab \xe3\x83\x8a'
# '\xe3\x82\xbf \xe3\x83\xa2 \xe3\x82\xbf \xe3\x83\xaf'

