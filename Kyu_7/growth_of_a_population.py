def nb_year(p0, percent, aug, p):
    percent /= 100.0
    years = 0
    while p0 < p:
        p0 += p0 * percent + aug
        years += 1
    return years
