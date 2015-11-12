from re import compile, search

REGEX = compile(r'(?P<num>\d+)$')


def increment_string(strng):
    m = search(REGEX, strng)
    if m:
        num = m.group('num')
        return '{}{:0>{}}'.format(strng[:m.start()], int(num) + 1, len(num))
    return '{}1'.format(strng)


assert increment_string('foo') == 'foo1'
assert increment_string('foobar23') == 'foobar24'
assert increment_string('foo0042') == 'foo0043'
assert increment_string('foo9') == 'foo10'
assert increment_string('foo099') == 'foo100'
assert increment_string('foobar00') == 'foobar01'
assert increment_string("foobar001") == "foobar002"
assert increment_string("foobar1") == "foobar2"
assert increment_string("foobar99") == "foobar100"
assert increment_string("") == "1"
