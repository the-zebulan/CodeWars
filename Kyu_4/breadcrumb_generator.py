from re import compile, findall

HREF = '<a href="{}">{}</a>'.format
IGNORE = ('the', 'of', 'in', 'from', 'by', 'with',
          'and', 'or', 'for', 'to', 'at', 'a')
SPAN = '<span class="active">{}</span>'.format
REGEX = compile(r'(?<!:/)/((?!index)[a-zA-Z-_]+)')


def generate_bc(url, separator):
    groups = findall(REGEX, url)
    if not groups:
        return SPAN('HOME')
    link = ['/']
    length = len(groups)
    result = [HREF('/', 'HOME')]
    for i, a in enumerate(groups, 1):
        if len(a) <= 30:
            txt = a.upper().replace('-', ' ')
        else:
            txt = ''.join(b[0] for b in a.split('-') if b not in IGNORE).upper()
        link.append(a + '/')
        result.append(HREF(''.join(link), txt) if i < length else SPAN(txt))
    return separator.join(result)
