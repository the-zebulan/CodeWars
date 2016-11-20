def print_nums(*args):
    try:
        fmt = '{{:0>{}}}'.format(len(str(max(args)))).format
    except ValueError:
        return ''
    return '\n'.join(fmt(a) for a in args)
