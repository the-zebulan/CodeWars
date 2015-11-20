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


assert shortener('No one expects the Spanish Inquisition! Our chief weapon is '
                 'surprise, fear and surprise; two chief weapons, fear, '
                 'surprise, and ruthless efficiency! And that will be it.') \
    == 'No one expects the Spanish Inquisition! Our chief weapon is surprise' \
       ', fear and surprise; two chief weapons, fear,Surprise,AndRuthless' \
       'Efficiency!AndThatWillBeIt.'

assert shortener('SMS messages are limited to 160 characters. It tends to be '
                 'irritating, especially when freshly written message is 164 '
                 'characters long. SMS messages are limited to 160 characters'
                 '. It tends to be irritating, especially when freshly '
                 'written message is 164 characters long.') \
    == 'SMSMessagesAreLimitedTo160Characters.ItTendsToBeIrritating,Especially' \
       'WhenFreshlyWrittenMessageIs164CharactersLong.SMSMessagesAreLimitedTo' \
       '160Characters.ItTendsToBeIrritating,EspeciallyWhenFreshlyWritten' \
       'MessageIs164CharactersLong.'
