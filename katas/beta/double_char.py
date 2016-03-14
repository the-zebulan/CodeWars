OUTPUT = '{0}{0}'.format


def double_char(s):
    return ''.join(OUTPUT(a) for a in s)
