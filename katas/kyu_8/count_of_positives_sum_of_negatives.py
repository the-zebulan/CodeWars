def count_positives_sum_negatives(arr):
    neg = pos = 0
    for a in arr:
        if a > 0:
            pos += 1
        else:
            neg += a
    return [pos, neg]
