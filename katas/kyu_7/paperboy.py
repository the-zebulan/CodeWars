DELIVERY_COST = ((40, 385), (20, 193), (10, 97), (5, 49), (1, 10))


def cheapest_quote(n):
    result = 0
    for total_newspapers, cost_of_newspapers in DELIVERY_COST:
        q, r = divmod(n, total_newspapers)
        if q:
            n -= q * total_newspapers
            result += q * cost_of_newspapers
        if not r:
            break
    return result / 100.0
