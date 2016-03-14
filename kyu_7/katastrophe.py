def strong_enough(earthquake, age):
    magnitude = reduce(lambda a, b: a * b, (sum(c) for c in earthquake))
    strength = 1000 * 0.99 ** age
    return 'Needs Reinforcement!' if magnitude > strength else 'Safe!'
