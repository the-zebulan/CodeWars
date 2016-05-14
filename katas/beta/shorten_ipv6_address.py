import re

REGEX = re.compile(r'((?:^|:)[0:]+(?::|$))')


def shorten(ip):
    result = ':'.join(a.lstrip('0') or '0'
                      for i, a in enumerate(ip.split(':')))
    try:
        return result.replace(max(REGEX.findall(result),
                                  key=lambda b: b.count('0')), '::', 1)
    except ValueError:
        return result
