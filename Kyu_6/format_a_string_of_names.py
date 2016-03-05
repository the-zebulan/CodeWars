def namelist(names):
    if not names:
        return ''
    names = [a['name'] for a in names]
    if len(names) > 1:
        return '{} & {}'.format(', '.join(names[:-1]), names[-1])
    return names[0]
