def substring_test(*args):
    shorter, longer = sorted((a.lower() for a in args), key=len)
    for b in xrange(len(shorter) - 1):
        if longer.find(shorter[b:b + 2]) != -1:
            return True
    return False
