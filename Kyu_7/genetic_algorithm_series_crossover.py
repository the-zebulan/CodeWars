def crossover(chromosome1, chromosome2, index):
    return [chromosome1[:index] + chromosome2[index:],
            chromosome2[:index] + chromosome1[index:]]


assert crossover("110", "001", 2) == ["111", "000"]
assert crossover("111000", "000110", 3) == ["111110", "000000"]
