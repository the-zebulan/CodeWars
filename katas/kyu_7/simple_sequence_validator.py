def validate_sequence(seq):
    return len({a - b for a, b in zip(seq, seq[1:])}) == 1
