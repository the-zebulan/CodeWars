def prefill(n, v=None):
    try:
        return [v] * int(n)
    except (TypeError, ValueError):
        raise TypeError('{} is invalid'.format(n))
