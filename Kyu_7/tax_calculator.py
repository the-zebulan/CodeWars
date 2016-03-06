def tax_calculator(total):
    if not isinstance(total, (float, int)) or total <= 0:
        return 0
    q, r = divmod(total, 10)
    less_equal_3 = q <= 3
    left = int(q) if less_equal_3 else 3
    return round(sum(a * tax for a, tax in zip(
        [10] * left + [r if less_equal_3 else total - (left * 10)],
        (0.1, 0.07, 0.05, 0.03))), 2)
