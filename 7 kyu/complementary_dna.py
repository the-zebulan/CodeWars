from string import maketrans

DNA = maketrans('ACGT', 'TGCA')
DNA_strand = lambda a: a.translate(DNA)

assert DNA_strand("AAAA") == "TTTT"
assert DNA_strand("ATTGC") == "TAACG"
assert DNA_strand("GTAT") == "CATA"
