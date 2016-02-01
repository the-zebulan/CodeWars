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


assert longest_consec(
    ['zone', 'abigail', 'theta', 'form', 'libe', 'zas'], 2) == 'abigailtheta'
assert longest_consec(
    ['ejjjjmmtthh', 'zxxuueeg', 'aanlljrrrxx', 'dqqqaaabbb',
     'oocccffuucccjjjkkkjyyyeehh'], 1) == 'oocccffuucccjjjkkkjyyyeehh'
assert longest_consec([], 3) == ''
assert longest_consec(['itvayloxrp', 'wkppqsztdkmvcuwvereiupccauycnjutlv',
                      'vweqilsfytihvrzlaodfixoyxvyuyvgpck'], 2) == \
      'wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck'
assert longest_consec(
    ['wlwsasphmxx', 'owiaxujylentrklctozmymu', 'wpgozvxxiu'], 2) == \
      'wlwsasphmxxowiaxujylentrklctozmymu'
assert longest_consec(
    ['zone', 'abigail', 'theta', 'form', 'libe', 'zas'], -2) == ''
assert longest_consec(['it', 'wkppv', 'ixoyx', '3452', 'zzzzzzzzzzzz'], 3) == \
      'ixoyx3452zzzzzzzzzzzz'
assert longest_consec(
    ['it', 'wkppv', 'ixoyx', '3452', 'zzzzzzzzzzzz'], 15) == ''
assert longest_consec(
    ['it', 'wkppv', 'ixoyx', '3452', 'zzzzzzzzzzzz'], 0) == ''
