def make_sentences(parts):
    return '{}.'.format(
        ''.join(' ' + a if a.isalnum() else a for a in parts).strip(' .'))
