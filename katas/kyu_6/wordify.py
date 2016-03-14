WORD = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
        7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
        12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
        16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
        20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
        70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred'}
KEYS = WORD.keys()[::-1]  # highest to lowest (100 - 1)


def wordify(n):
    result = []
    for key in KEYS:
        quo, rem = divmod(n, key)
        if quo:
            if key == 100:
                result.append(WORD[quo])
            result.append(WORD[key])
            n = rem
    return ' '.join(result)
