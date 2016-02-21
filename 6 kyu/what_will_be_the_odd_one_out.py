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


assert odd_one_out('Hello World') == ['H', 'e', ' ', 'W', 'r', 'l', 'd']
assert odd_one_out('Codewars') == ['C', 'o', 'd', 'e', 'w', 'a', 'r', 's']
assert odd_one_out('woowee') == []
assert odd_one_out('wwoooowweeee') == []
assert odd_one_out('racecar') == ['e']
assert odd_one_out('Mamma') == ['M']
assert odd_one_out('Mama') == ['M', 'm']
