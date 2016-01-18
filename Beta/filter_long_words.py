def filter_long_words(sentence, n):
    return filter(lambda a: len(a) > n, sentence.split())


assert filter_long_words('The quick brown fox jumps over the lazy dog', 4) \
    == ['quick', 'brown', 'jumps']
