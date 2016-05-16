from collections import Counter


def find_discounted(prices):
    count_prices = dict(Counter(int(a) for a in prices.split()))
    result = []
    for key in sorted(count_prices):
        value = count_prices[key]
        try:
            count_prices[int(key / 0.75)] -= value
        except KeyError:
            continue
        result.extend(key for _ in xrange(value if key else 1))
    return ' '.join(str(b) for b in result)
