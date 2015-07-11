def DNAtoRNA(dna):
    """ dna_to_rna == PEP8 (forced camelCase by codewars) """
    return dna.replace('T', 'U')

assert DNAtoRNA('TTTT') == 'UUUU'
assert DNAtoRNA('GCAT') == 'GCAU'
assert DNAtoRNA('GACCGCCGCC') == 'GACCGCCGCC'
