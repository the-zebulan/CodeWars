from re import compile, IGNORECASE, sub

REGEX = compile('(bad|mean|ugly|horrible|hideous)', flags=IGNORECASE)


def filter_words(phrase):
    return sub(REGEX, 'awesome', phrase)
