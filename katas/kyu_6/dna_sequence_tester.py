from string import maketrans

TABLE = maketrans('ATGC', 'TACG')


def check_DNA(seq1, seq2):
    one, two = sorted((seq1, seq2), key=len)
    return one.translate(TABLE) in two[::-1]
