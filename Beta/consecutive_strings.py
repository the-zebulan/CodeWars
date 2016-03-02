def longest_consec(lst, k):
    if not lst or k > len(lst) or k <= 0:
        return ''
    lengths = [len(a) for a in lst]
    dex = left = maximum = total = 0
    for i, b in enumerate(lengths, 1):
        total += b
        if i >= k:
            if total > maximum:
                maximum = total
                dex = i
            total -= lengths[left]
            left += 1
    return ''.join(lst[dex - k:dex])
