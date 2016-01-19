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


assert mix("my&friend&Paul has heavy hats! &",
           "my friend John has many many friends &") \
    == "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
assert mix("mmmmm m nnnnn y&friend&Paul has heavy hats! &",
           "my frie n d Joh n has ma n y ma n y frie n ds n&") \
    == "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
assert mix("Are the kids at home? aaaaa fffff",
           "Yes they are here! aaaaa fffff") \
    == "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
assert mix("Are they here", "yes, they are here") == "2:eeeee/2:yy/=:hh/=:rr"
assert mix("looping is fun but dangerous", "less dangerous than coding") \
    == "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"
assert mix(" In many languages", " there's a pair of functions") \
    == "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"
assert mix("Lords of the Fallen", "gamekult") == "1:ee/1:ll/1:oo"
assert mix("codewars", "codewars") == ""
assert mix("A generation must confront the looming ", "codewarrs") \
    == "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"
