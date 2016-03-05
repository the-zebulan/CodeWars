# def title_case(title, minor_words=''):
#     if not minor_words:
#         return title.title()
#     result = []
#     minor_words = minor_words.lower().split()
#     for i, a in enumerate(title.split()):
#         current = a.lower()
#         if i != 0 and current in minor_words:
#             result.append(current)
#         else:
#             result.append(current.title())
#     return ' '.join(result)


def title_case(title, minor_words=''):
    """ Thanks to 'soapie' from CodeWars """
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join(word if word in minor_words else word.capitalize()
                    for word in title)
