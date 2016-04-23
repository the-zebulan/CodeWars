from itertools import product


ADJACENT = {'1': '124', '2': '1235', '3': '236', '4': '1475', '5': '24568',
            '6': '3569', '7': '478', '8': '05789', '9': '689', '0': '08'}


def get_pins(observed):
    return [''.join(a) for a in product(*(ADJACENT[b] for b in observed))]
