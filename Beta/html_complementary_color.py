def get_reversed_color(hex_color):
    if not isinstance(hex_color, str) or len(hex_color) >= 7:
        raise ValueError
    return '#{:06X}'.format(0xffffff - int(hex_color or '0', 16))


assert get_reversed_color('01fD08') == '#FE02F7'
assert get_reversed_color('') == '#FFFFFF'
assert get_reversed_color('a23') == '#FFF5DC'
