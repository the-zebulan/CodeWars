from itertools import groupby


def run_length_encoding(string):
    return [[sum(1 for _ in g), k] for k, g in groupby(string)]
