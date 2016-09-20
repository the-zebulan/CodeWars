def hex_color(codes):
    try:
        r, g, b = (int(a) for a in codes.split())
    except ValueError:
        return 'black'
    if r == g == b:
        return 'black' if r == 0 else 'white'
    if r > g and r > b:
        return 'red'
    elif g > r and g > b:
        return 'green'
    elif b > r and b > g:
        return 'blue'
    elif r == g:
        return 'yellow'
    elif g == b:
        return 'cyan'
    elif b == r:
        return 'magenta'
