from operator import truediv


def representation(zone_pop, rep_req):
    rep_total = 0
    result = []
    population_total = sum(zone_pop)
    for population in zone_pop:
        # rep = (population / population_total) * rep_req  # Python 3
        rep = truediv(population, population_total) * rep_req
        # current = round(rep) or 1  # Python 3
        current = round(rep) if rep % 1 > 0.5 else int(rep) or 1
        rep_total += current
        result.append(current)
    diff = rep_total - rep_req
    # for _ in range(abs(int(diff))):  # Python 3
    for _ in xrange(abs(int(diff))):
        if diff < 0:
            result[result.index(min(result))] += 1
            diff += 1
        else:
            result[result.index(max(result))] -= 1
            diff -= 1
    return result
