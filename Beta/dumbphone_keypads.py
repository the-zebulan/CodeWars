KEYPAD = {
    ' ': '0', '0': '00', '1': '1', '2': '2222', '3': '3333', '4': '4444',
    '5': '5555', '7': '77777', '8': '8888', '9': '99999', 'A': '2', 'B': '22',
    'C': '222', 'D': '3', 'E': '33', 'F': '333', 'G': '4', 'H': '44',
    'I': '444', 'J': '5', 'K': '55', 'L': '555', 'M': '6', 'N': '66',
    'O': '666', 'P': '7', 'Q': '77', 'R': '777', 'S': '7777', 'T': '8',
    'U': '88', 'V': '888', 'W': '9', 'X': '99', 'Y': '999', 'Z': '9999'
}
OUTPUT = '{}{}'.format


def sequence(phrase):
    prev = None
    result = []
    for a in phrase.upper():
        current = KEYPAD.get(a, a)
        first = current[0]
        result.append(OUTPUT('p' if first == prev else '', current))
        prev = first
    return ''.join(result)
