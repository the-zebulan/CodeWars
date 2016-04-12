def short_form(s):
    return '{}{}{}'.format(s[0], s[1:-1].translate(None, 'aeiouAEIOU'), s[-1])
