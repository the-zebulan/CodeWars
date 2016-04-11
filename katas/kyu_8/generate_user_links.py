from urllib import quote

CODEWARS = 'http://www.codewars.com/users/{}'.format


def generate_link(user):
    return CODEWARS(quote(user))
