import __builtin__


def last(*args):
    end = args[-1]
    return end[-1] if isinstance(end, (__builtin__.str, list, tuple)) else end
