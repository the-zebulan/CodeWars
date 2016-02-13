PAD_6 = '{:0>6}'.format
TO_HEX = '{:02X}'.format


def get_reversed_color(hex_color):
    if not isinstance(hex_color, str) or len(hex_color) >= 7:
        raise ValueError
    padded = PAD_6(hex_color)
    return '#{}'.format(''.join(TO_HEX(255 - int(padded[a:a + 2], 16))
                                for a in xrange(0, 6, 2)))


assert get_reversed_color('01fD08') == '#FE02F7'
assert get_reversed_color('') == '#FFFFFF'
assert get_reversed_color('a23') == '#FFF5DC'
