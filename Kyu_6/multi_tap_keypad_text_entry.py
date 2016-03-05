KEY_PRESSES = {
    '1ADGJMPTW* #': 1,
    'BEHKNQUX0': 2,
    'CFILORVY': 3,
    '23456S8Z': 4,
    '79': 5
}


def presses(phrase):
    total = 0
    for a in phrase.upper():
        for k, v in KEY_PRESSES.iteritems():
            if a in k:
                total += v
                break
    return total
