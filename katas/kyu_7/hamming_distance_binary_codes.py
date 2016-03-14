def hamming_distance(a, b):
    return sum(c != d for c, d in zip(a, b))
