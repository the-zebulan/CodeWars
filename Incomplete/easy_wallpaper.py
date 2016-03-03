from math import ceil

WORDS = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
         7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
         12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
         16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
         20: 'twenty'}


def wallpaper(l, w, h):
    pass
    # area = l * w * h
    # return WORDS[int(ceil((area + (area * 0.15)) / 5.2))]


assert wallpaper(6.3, 4.5, 3.29) == "sixteen"
assert wallpaper(7.8, 2.9, 3.29) == "sixteen"
assert wallpaper(6.3, 5.8, 3.13) == "seventeen"
assert wallpaper(6.1, 6.7, 2.81) == "sixteen"
