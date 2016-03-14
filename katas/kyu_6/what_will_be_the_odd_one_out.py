from collections import Counter


def odd_one_out(s):
    # wrote this before I realized this kata was JavaScript only!
    pairs = {k: [k] * (v / 2 * 2) for k, v in Counter(s).iteritems()}
    result = []
    for a in s:
        try:
            pairs[a].pop()
        except IndexError:
            result.append(a)
    return result
