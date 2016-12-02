def highest_value(*args):
    return max(args, key=lambda a: sum(ord(b) for b in a))
