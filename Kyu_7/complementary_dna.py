from string import maketrans

DNA = maketrans('ACGT', 'TGCA')


def DNA_strand(string):
    """ dna_strand == PEP8 (forced naming by CodeWars) """
    return string.translate(DNA)
