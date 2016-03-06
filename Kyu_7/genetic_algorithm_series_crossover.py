def crossover(chromosome1, chromosome2, index):
    return [chromosome1[:index] + chromosome2[index:],
            chromosome2[:index] + chromosome1[index:]]
