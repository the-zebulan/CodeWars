def what_is(x):
    if x == 42:
        return 'everything'
    elif x == 42 * 42:
        return 'everything squared'
    return 'nothing'

assert what_is(0) == 'nothing'
assert what_is(123) == 'nothing'
assert what_is(-1) == 'nothing'
assert what_is(42) == 'everything'
assert what_is(42 * 42) == 'everything squared'
