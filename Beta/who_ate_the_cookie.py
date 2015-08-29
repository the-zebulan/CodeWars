def cookie(x):
    if isinstance(x, str):
        who = 'Zach'
    elif type(x) in (float, int):
        who = 'Monica'
    else:
        who = 'the dog'
    return 'Who ate the last cookie? It was {}!'.format(who)

assert cookie("Ryan") == "Who ate the last cookie? It was Zach!"
assert cookie(2.3) == "Who ate the last cookie? It was Monica!"
assert cookie(26) == "Who ate the last cookie? It was Monica!"
assert cookie(True) == "Who ate the last cookie? It was the dog!"
