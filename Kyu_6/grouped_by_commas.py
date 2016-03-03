def group_by_commas(n):
    return '{:,}'.format(n)

assert group_by_commas(1) == '1'
assert group_by_commas(10) == '10'
assert group_by_commas(100) == '100'
assert group_by_commas(1000) == '1,000'
assert group_by_commas(10000) == '10,000'
assert group_by_commas(100000) == '100,000'
assert group_by_commas(1000000) == '1,000,000'
assert group_by_commas(35235235) == '35,235,235'
