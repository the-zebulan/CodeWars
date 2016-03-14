def diamond(n):
    if n % 2 == 0 or n <= 0:
        return None
    output = '{}{}\n'.format
    rows = []
    stars = 1
    for spaces in xrange(n / 2, -1, -1):
        rows.append(output(spaces * ' ', stars * '*'))
        stars += 2
    return ''.join((rows + rows[:-1][::-1]))
