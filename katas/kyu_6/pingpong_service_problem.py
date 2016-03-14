def service(score):
    total = sum(int(a) for a in score.split(':'))
    return ('first', 'second')[(total / (5 if total < 40 else 2)) % 2]
