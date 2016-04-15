OUTPUT = "I don't think you {} today, I think you {} {} {}!".format


def alan_annoying_kid(phrase):
    words = phrase.split()
    action = ' '.join(words[2:]).rstrip('.')
    if "didn't" in phrase:
        return OUTPUT(action, 'did', words[3], 'it')
    return OUTPUT(action, "didn't", words[2][:-2], 'at all')
