def search(budget, prices):
    return ','.join(str(a) for a in sorted(prices) if a <= budget)
