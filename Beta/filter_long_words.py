def filter_long_words(sentence, n):
    return filter(lambda a: len(a) > n, sentence.split())
