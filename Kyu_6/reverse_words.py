def reverse_words(string):
    return ' '.join(a[::-1] for a in string.split(' '))

assert reverse_words('The quick brown fox jumps over the lazy dog.') == \
    'ehT kciuq nworb xof spmuj revo eht yzal .god'
assert reverse_words('This is an example!') == 'sihT si na !elpmaxe'
