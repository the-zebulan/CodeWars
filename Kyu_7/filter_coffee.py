def search(budget, prices):
    return ','.join(str(a) for a in sorted(prices) if a <= budget)

assert search(3, [6, 1, 2, 9, 2]) == '1,2,2'
assert search(14, [7, 3, 23, 9, 14, 20, 7]) == '3,7,7,9,14'
assert search(0, [6, 1, 2, 9, 2]) == ''
assert search(10, []) == ''
assert search(24, [24, 0, 100, 2, 5]) == '0,2,5,24'
