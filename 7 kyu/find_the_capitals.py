def capitals(word):
    return [i for i, a in enumerate(word) if a.isupper()]

assert capitals('CoDeWaRs') == [0, 2, 4, 6]
