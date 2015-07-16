from re import split


def drop_cap(string):
    return ''.join(a.capitalize() if not a.isspace() and len(a) > 2 else a
                   for a in split(r'(\s+)', string))

assert drop_cap('more  than    one space between words') == \
       'More  Than    One Space Between Words'
assert drop_cap('aRQh yBdbvhcRglvirAcRpXat NlahSCaPlMkol') == \
       'Arqh Ybdbvhcrglviracrpxat Nlahscaplmkol'
