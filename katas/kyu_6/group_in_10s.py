def group_in_10s(*args):
    if not args:
        return []
    args = sorted(args)
    result = [None] * (args[-1] / 10 + 1)
    for arg in args:
        dex = arg / 10
        try:
            result[dex].append(arg)
        except AttributeError:
            result[dex] = [arg]
    return result
