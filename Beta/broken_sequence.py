def find_missing_number(sequence):
    if not sequence:
        return 0
    try:
        sequence = set(int(a) for a in sequence.split())
    except ValueError:
        return 1
    for b in xrange(1, max(sequence) + 1):
        if b not in sequence:
            return b
    return 0
