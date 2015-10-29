from string import maketrans

DNA = maketrans('ACGT', 'TGCA')


def DNA_strand(string):
    """ dna_strand == PEP8 (forced naming by CodeWars) """
    return string.translate(DNA)

assert DNA_strand("AAAA") == "TTTT"
assert DNA_strand("ATTGC") == "TAACG"
assert DNA_strand("GTAT") == "CATA"
