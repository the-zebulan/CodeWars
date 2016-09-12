def get_length_of_missing_array(arr):
    if not arr:
        return 0
    lengths = []
    for a in arr:
        if not a:
            return 0
        lengths.append(len(a))
    lengths.sort()
    for b, c in zip(lengths, lengths[1:]):
        if b + 1 != c:
            return b + 1
