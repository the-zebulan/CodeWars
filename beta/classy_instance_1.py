def show_me(instname):
    attrs = sorted(instname.__dict__.iterkeys())
    if len(attrs) == 1:
        attrs = attrs[0]
    else:
        attrs = '{} and {}'.format(', '.join(attrs[:-1]), attrs[-1])
    return 'Hi, I\'m one of those {}s! Have a look at my {}.'\
        .format(instname.__class__.__name__, attrs)
