def convert_num(number, base):
    try:
        return {'hex': hex, 'bin': bin}[base](number)
    except KeyError:
        return 'Invalid base input'
    except TypeError:
        return 'Invalid {} input'.format(
            ('base', 'number')[isinstance(base, str)]
        )
