LOWER_VOWELS = 'aeiou'


# def shortcut(string):
#     return filter(lambda a: a not in LOWER_VOWELS, string)


def shortcut(string):
    return string.translate(None, LOWER_VOWELS)
