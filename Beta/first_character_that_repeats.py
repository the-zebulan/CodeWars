from collections import Counter


def first_dup(s):
    cnt = Counter(s)
    for a in s:
        if cnt[a] >= 2:
            return a


assert first_dup('like') is None
assert first_dup('tweet') == 't'
assert first_dup('Ode to Joy') == ' '
assert first_dup('ode to joy') == 'o'
assert first_dup('bar') is None
assert first_dup('123123') == '1'
assert first_dup('!@#$!@#$') == '!'
assert first_dup('1a2b3a3c') == 'a'
