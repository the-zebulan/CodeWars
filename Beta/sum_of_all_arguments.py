def sum_all(*args):
    try:
        return sum(args)
    except TypeError:
        return False
