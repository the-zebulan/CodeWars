def get_reversed_color(hex_color):
    if not isinstance(hex_color, str) or len(hex_color) >= 7:
        raise ValueError
    return '#{:06X}'.format(0xffffff - int(hex_color or '0', 16))
