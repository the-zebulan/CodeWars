def luck_check(s):
    q, r = divmod(len(s), 2)
    return sum(int(a) for a in s[:q]) == sum(int(b) for b in s[q + r:])


assert luck_check('683179') is True
assert luck_check('683000') is False
