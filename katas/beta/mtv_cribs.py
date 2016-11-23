def my_crib(n):
    floor = '|{}|'.format
    roof = '/{}\\'.format
    inner_width = n * 2
    outer_width = inner_width + 2
    result = []
    for a in xrange(0, n * 2, 2):
        result.append(roof(' ' * a).center(outer_width))
    result.append(roof('_' * inner_width))
    for _ in xrange(n - 1):
        result.append(floor(' ' * inner_width))
    result.append(floor('_' * inner_width))
    return '\n'.join(result)
