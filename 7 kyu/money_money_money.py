def calculate_years(principal, interest, tax, desired):
    years = 0
    while True:
        if principal >= desired:
            return years
        interest_earned = principal * interest
        principal += interest_earned - (interest_earned * tax)
        years += 1


assert calculate_years(1000, 0.05, 0.18, 1100) == 3
assert calculate_years(1000, 0.01625, 0.18, 1200) == 14
assert calculate_years(1000, 0.05, .18, 1000) == 0
