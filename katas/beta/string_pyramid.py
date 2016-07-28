def watch_pyramid_from_the_side(characters):
    if not characters:
        return characters
    width = 2 * len(characters) - 1
    output = '{{:^{}}}'.format(width).format
    return '\n'.join(output(char * dex) for char, dex in
                     zip(reversed(characters), xrange(1, width + 1, 2)))


def watch_pyramid_from_above(characters):
    if not characters:
        return characters
    width = 2 * len(characters) - 1
    dex = width - 1  # maximum index possible, width & height
    result = []
    for a in xrange(width):
        row = []
        for b in xrange(width):
            minimum, maximum = sorted((a, b))
            row.append(characters[min(abs(dex - maximum), abs(0 - minimum))])
        result.append(''.join(row))
    return '\n'.join(result)


def count_visible_characters_of_the_pyramid(characters):
    if not characters:
        return -1
    return (2 * len(characters) - 1) ** 2


def count_all_characters_of_the_pyramid(characters):
    if not characters:
        return -1
    return sum(a ** 2 for a in xrange(1, 2 * len(characters), 2))
