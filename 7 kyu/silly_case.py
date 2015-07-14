def sillycase(silly):
    mid = (len(silly) + 1) / 2
    return '{}{}'.format(silly[:mid].lower(), silly[mid:].upper())

assert sillycase('foobar') == 'fooBAR'
assert sillycase('codewars') == 'codeWARS'
assert sillycase('brian') == 'briAN'
