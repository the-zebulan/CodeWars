from collections import Counter


def mix(s1, s2):
    d = {}
    result = []
    for i, string in enumerate((s1, s2), 1):
        for k, v in Counter(string).iteritems():
            if k.islower() and v > 1:
                try:
                    value = d[k][0]
                    if v > value:
                        d[k] = v, i
                    elif v == value:
                        d[k] = v, 3
                except KeyError:
                    d[k] = v, i
    for k, (v, n) in sorted(d.iteritems(), key=lambda (k, (v, n)): (-v, n, k)):
        result.append('{}:{}'.format('=' if n == 3 else n, k * v))
    return '/'.join(result)
