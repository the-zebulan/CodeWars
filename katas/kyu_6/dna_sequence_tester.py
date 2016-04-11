from string import maketrans

TABLE = maketrans('ATCG', '0011')


def check_DNA(seq1, seq2):
    one, two = sorted((seq1.translate(TABLE), seq2.translate(TABLE)), key=len)
    return one in two[::-1]
