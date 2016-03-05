from re import split


def camelize(string):
    return ''.join(a.capitalize() for a in split('([^a-zA-Z0-9])', string)
                   if a.isalnum())
