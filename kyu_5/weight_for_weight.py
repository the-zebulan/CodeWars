def order_weight(string):
    return ' '.join(c[1] for c in sorted((sum(int(b) for b in a), a)
                                         for a in string.split()))
