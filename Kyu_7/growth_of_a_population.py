def nb_year(p0, percent, aug, p):
    percent /= 100.0
    years = 0
    while p0 < p:
        p0 += p0 * percent + aug
        years += 1
    return years

assert nb_year(1500, 5, 100, 5000) == 15
assert nb_year(1500000, 2.5, 10000, 2000000) == 10
assert nb_year(1500000, 0.25, 1000, 2000000) == 94
