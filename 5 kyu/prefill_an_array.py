def prefill(n, v=None):
    try:
        return [v] * int(n)
    except (TypeError, ValueError):
        raise TypeError('{} is invalid'.format(n))

assert prefill(3, 1) == [1, 1, 1]
assert prefill(2, 'abc') == ['abc', 'abc']
assert prefill('1', 1) == [1]
assert prefill(3, prefill(2, '2d')) == \
    [['2d', '2d'], ['2d', '2d'], ['2d', '2d']]
