def is_divisible(*args):
    n = args[0]
    return all(n % a == 0 for a in args[1:])
