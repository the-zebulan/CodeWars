def service(score):
    total = sum(int(a) for a in score.split(':'))
    return ('first', 'second')[(total / (5 if total < 40 else 2)) % 2]


assert service('0:0') == 'first'
assert service('0:5') == 'second'
assert service('3:2') == 'second'
assert service('5:5') == 'first'
assert service('11:11') == 'first'
assert service('14:15') == 'second'
assert service('21:20') == 'first'
assert service('21:22') == 'second'
