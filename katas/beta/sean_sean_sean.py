def sean(s):
    if not isinstance(s, str):
        return 'Boo! Not a string, boo!'
    return "Ohhhhh it's {}".format(' '.join(
        'Sean!' if a[0].islower() else 'SEAN!' for a in s.split()[2:]
    ) or 'Sean!')
