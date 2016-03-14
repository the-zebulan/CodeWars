def cookie(x):
    if isinstance(x, str):
        who = 'Zach'
    elif type(x) in (float, int):
        who = 'Monica'
    else:
        who = 'the dog'
    return 'Who ate the last cookie? It was {}!'.format(who)
