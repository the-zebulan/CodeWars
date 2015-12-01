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


assert generate_bc('https://codewars.com/insider-the-the-transmutation-from-and'
                   '/wanted/diplomatic-bioengineering/at-from-surfer-'
                   'cauterization-skin', ' - ') \
    == '<a href="/">HOME</a> - <a href="/insider-the-the-transmutation-from-' \
       'and/">IT</a> - <a href="/insider-the-the-transmutation-from-and/want' \
       'ed/">WANTED</a> - <a href="/insider-the-the-transmutation-from-and/w' \
       'anted/diplomatic-bioengineering/">DIPLOMATIC BIOENGINEERING</a> - <s' \
       'pan class="active">SCS</span>'
assert generate_bc('http://www.agcpartners.co.uk', ' % ') \
    == '<span class="active">HOME</span>'
assert generate_bc('https://www.agcpartners.co.uk/', ' >>> ') \
    == '<span class="active">HOME</span>'
assert generate_bc('www.agcpartners.co.uk', ' # ') \
    == '<span class="active">HOME</span>'
assert generate_bc('www.agcpartners.co.uk/', ' * ') \
    == '<span class="active">HOME</span>'
assert generate_bc("mysite.com/pictures/holidays.html", " : ") \
    == '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : ' \
       '<span class="active">HOLIDAYS</span>'

assert generate_bc("www.codewars.com/users/GiacomoSorbi", " / ") \
    == '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class=' \
       '"active">GIACOMOSORBI</span>'

assert generate_bc("www.microsoft.com/docs/index.htm", " * ") \
    == '<a href="/">HOME</a> * <span class="active">DOCS</span>'

assert generate_bc("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-"
                   "example/example.htm", " > ") \
    == '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-' \
       'meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>'

assert generate_bc("www.very-long-site_name-to-make-a-silly-yet-meaningful-"
                   "example.com/users/giacomo-sorbi", " + ") \
    == '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class=' \
       '"active">GIACOMO SORBI</span>'

assert generate_bc(
    'www.microsoft.com/important/confidential/docs/index.htm#top', ' * ') \
    == '<a href="/">HOME</a> * <a href="/important/">IMPORTANT</a> * ' \
       '<a href="/important/confidential/">CONFIDENTIAL</a> * ' \
       '<span class="active">DOCS</span>'
