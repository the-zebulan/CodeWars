def hamming_distance(a, b):
    return sum(c != d for c, d in zip(a, b))

assert hamming_distance('100101', '101001') == 2
assert hamming_distance('1010', '0101') == 4
assert hamming_distance('100101011011010010010', '101100010110010110101') == 9
