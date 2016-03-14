def max_rot(n):
    maximum = n
    s = list(str(n))
    for i in xrange(len(s) - 1):
        s.append(s.pop(i))
        current = int(''.join(s))
        if current > maximum:
            maximum = current
    return maximum
