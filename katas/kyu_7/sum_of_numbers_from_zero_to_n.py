def show_sequence(n):
    if n == 0:
        return '0=0'
    elif n < 0:
        return '{}<0'.format(n)
    return '{} = {}'.format(
        '+'.join(str(a) for a in xrange(n + 1)), n * (n + 1) // 2
    )
