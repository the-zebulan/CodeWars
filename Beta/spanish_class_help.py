def gender(*nouns):
    result = []
    for noun in nouns:
        if not isinstance(noun, str):
            result.append(noun)
            continue
        elif noun.endswith('a'):
            prefix = 'la'
        elif noun.endswith('as'):
            prefix = 'las'
        elif noun.endswith('s'):
            prefix = 'los'
        else:
            prefix = 'el'
        result.append('{} {}'.format(prefix, noun))
    return result


assert gender('genio') == ['el genio']
assert gender('chico', 'esquinas') == ['el chico', 'las esquinas']
assert gender("parques") == ['los parques']
assert gender("vino", 5, None) == ['el vino', 5, None]
assert gender('lampas') == ["las lampas"]
