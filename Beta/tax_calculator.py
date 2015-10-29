def tax_calculator(total):
    if not isinstance(total, (float, int)) or total <= 0:
        return 0
    q, r = divmod(total, 10)
    less_equal_3 = q <= 3
    left = int(q) if less_equal_3 else 3
    return round(sum(a * tax for a, tax in zip(
        [10] * left + [r if less_equal_3 else total - (left * 10)],
        (0.1, 0.07, 0.05, 0.03))), 2)


assert tax_calculator(1) == 0.1
assert tax_calculator(10) == 1

assert tax_calculator(11) == 1.07
assert tax_calculator(15) == 1.35
assert tax_calculator(18) == 1.56

assert tax_calculator(21) == 1.75
assert tax_calculator(26) == 2
assert tax_calculator(30) == 2.2

assert tax_calculator(30.49) == 2.21
assert tax_calculator(35) == 2.35
assert tax_calculator(100) == 4.3
assert tax_calculator(1000000) == 30001.3

assert tax_calculator(0) == 0
assert tax_calculator(-3) == 0
assert tax_calculator(None) == 0
assert tax_calculator('monkey') == 0
