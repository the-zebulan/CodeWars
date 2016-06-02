from string import maketrans


def reverse_complement(dna):
    if not set('ACTG').issuperset(dna):
        return 'Invalid sequence'
    return dna[::-1].translate(maketrans('ACTG', 'TGAC'))
