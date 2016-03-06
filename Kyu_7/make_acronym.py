# def make_acronym(phrase):
#     if not isinstance(phrase, str):
#         return 'Not a string'
#     words = phrase.split()
#     result = []
#     for word in words:
#         if not word.isalpha():
#             return 'Not letters'
#         result.append(word[0].upper())
#     return ''.join(result)


def make_acronym(phrase):
    try:
        return ''.join(word[0].upper() if word.isalpha() else 0
                       for word in phrase.split())
    except AttributeError:
        return 'Not a string'
    except TypeError:
        return 'Not letters'
