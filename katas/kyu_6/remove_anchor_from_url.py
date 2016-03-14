from re import compile, match

REGEX = compile('www\.\w+\.[^#]+')


def remove_url_anchor(url):
    return match(REGEX, url).group(0)


# def remove_url_anchor(url):
#     return url.split('#')[0]
