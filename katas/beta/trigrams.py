def trigrams(phrase):
    phrase = phrase.replace(' ', '_')
    return ' '.join(phrase[a:a + 3] for a in xrange(len(phrase) - 2))
