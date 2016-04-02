DOGS = ((100, '101 DALMATIONS!!!'), (50, 'Woah that\'s a lot of dogs!'),
        (10, 'More than a handful!'))


def how_many_dalmatians(n):
    return next((msg for dogs, msg in DOGS if n > dogs), 'Hardly any')
