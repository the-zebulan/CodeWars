from collections import MutableMapping


def flatten(d, parent_key='', sep='/'):
    result = []
    for k, v in d.iteritems():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            result.extend(flatten(v, new_key, sep=sep).iteritems())
        else:
            result.append((new_key, v))
    return dict(result) or {parent_key: ''}
