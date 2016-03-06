from itertools import izip_longest


def createDict(keys, values):
    """ create_dict == PEP8 (forced mixedCase by CodeWars) """
    if len(keys) > len(values):
        return dict(izip_longest(keys, values, fillvalue=None))
    return dict(zip(keys, values))
