def spam(number):
    return 'hue' * number

assert spam(1) == 'hue'
assert spam(6) == 'huehuehuehuehuehue'
assert spam(14) == 'huehuehuehuehuehuehuehuehuehuehuehuehuehue'
