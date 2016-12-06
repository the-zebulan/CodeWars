def discover_original_price(discounted_price, sale_percentage):
    return round(discounted_price / ((100 - sale_percentage) * 0.01), 2)
