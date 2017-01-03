def calculate_total(subtotal, tax, tip):
    return round(subtotal * (100 + tax + tip) / 100, 2)
