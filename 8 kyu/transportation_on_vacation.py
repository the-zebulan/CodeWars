def rental_car_cost(d):
    if d < 3:
        discount = 0
    elif d < 7:
        discount = 20
    else:
        discount = 50
    return 40 * d - discount


assert rental_car_cost(1) == 40
assert rental_car_cost(4) == 140
assert rental_car_cost(7) == 230
assert rental_car_cost(8) == 270
