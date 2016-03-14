def calculate_years(principal, interest, tax, desired):
    years = 0
    while True:
        if principal >= desired:
            return years
        interest_earned = principal * interest
        principal += interest_earned - (interest_earned * tax)
        years += 1
