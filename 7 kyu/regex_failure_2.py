from re import compile, IGNORECASE, sub

REGEX = compile('(bad|mean|ugly|horrible|hideous)', flags=IGNORECASE)


def filter_words(phrase):
    return sub(REGEX, 'awesome', phrase)

assert filter_words("You're Bad! timmy!") == "You're awesome! timmy!"
assert filter_words("You're MEAN! timmy!") == "You're awesome! timmy!"
