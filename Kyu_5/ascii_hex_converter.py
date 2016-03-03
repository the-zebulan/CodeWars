# HEX = '{:x}'.format
#
#
# class Converter(object):
#     @staticmethod
#     def to_ascii(s):
#         return ''.join(chr(int(s[a:a + 2], 16)) for a in xrange(0, len(s), 2))
#
#     @staticmethod
#     def to_hex(s):
#         return ''.join(HEX(ord(b)) for b in s)


class Converter(object):
    @staticmethod
    def to_ascii(s):
        return s.decode('hex')

    @staticmethod
    def to_hex(s):
        return s.encode('hex')


assert Converter.to_hex("Look mom, no hands") \
    == "4c6f6f6b206d6f6d2c206e6f2068616e6473"
assert Converter.to_ascii("4c6f6f6b206d6f6d2c206e6f2068616e6473") \
    == "Look mom, no hands"
