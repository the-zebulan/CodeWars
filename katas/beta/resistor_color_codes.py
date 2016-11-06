from operator import truediv


def decode_resistor_colors(bands):
    color_codes = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
                   'green': 5, 'blue': 6, 'violet': 7, 'gray': 8, 'white': 9}
    tolerances = {'gold': 5, 'silver': 10}
    try:
        band_1, band_2, band_3, tolerance = (
            color_codes.get(a, tolerances.get(a)) for a in bands.split())
    except ValueError:
        band_1, band_2, band_3 = (color_codes[b] for b in bands.split())
        tolerance = 20
    ohms = int(str(band_1) + str(band_2)) * (10 ** band_3)
    if ohms < 1000:
        ohms_output = ohms
    elif ohms < 1000000:
        ohms_output = '{:g}k'.format(truediv(ohms, 1000))
    else:
        ohms_output = '{:g}M'.format(truediv(ohms, 1000000))
    return '{} ohms, {}%'.format(ohms_output, tolerance)
