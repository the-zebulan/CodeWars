PIG = '{}{}ay'.format


def pig_it(s):
    return ' '.join(PIG(a[1:], a[0]) if a.isalpha() else a for a in s.split())
