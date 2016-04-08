from string import punctuation


def nothing_special(s):
    try:
        return s.translate(None, punctuation)
    except AttributeError:
        return 'Not a string!'
