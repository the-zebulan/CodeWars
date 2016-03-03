def rental_car_cost(d):
    return 40 * d - ((50, 20)[d < 7], 0)[d < 3]


assert rental_car_cost(1) == 40
assert rental_car_cost(4) == 140
assert rental_car_cost(7) == 230
assert rental_car_cost(8) == 270
