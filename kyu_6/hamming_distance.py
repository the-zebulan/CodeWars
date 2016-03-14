def hamming(a, b):
    return sum(c != d for c, d in zip(a, b))
