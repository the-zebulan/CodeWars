PIG = '{}{}ay'.format


def pig_it(s):
    return ' '.join(PIG(a[1:], a[0]) if a.isalpha() else a for a in s.split())


assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
assert pig_it('This is my string') == 'hisTay siay ymay tringsay'
