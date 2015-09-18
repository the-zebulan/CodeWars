def trigrams(phrase):
    phrase = phrase.replace(' ', '_')
    return ' '.join(phrase[a:a + 3] for a in xrange(len(phrase) - 2))

assert trigrams('the quick red') == \
    'the he_ e_q _qu qui uic ick ck_ k_r _re red'
assert not trigrams('Hi')
