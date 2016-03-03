def camel(s):
    result = []
    for i, word in enumerate(s.split()):
        if not word.isupper():
            result.append(word.title() if i else word.lower())
        else:
            result.append(word)
    return ''.join(result)


def shortener(message):
    spaces = []
    total_spaces = length = 0
    for i, a in enumerate(message):
        if a.isspace():
            spaces.append(i)
            total_spaces += 1
        length += 1

    if not spaces or length <= 160:
        return message

    diff = length - 160
    if total_spaces <= diff:
        return camel(message)

    mid = spaces[-(diff + 1):][0] + 1
    return '{}{}'.format(message[:mid], camel(message[mid:]))
