def rental_car_cost(d):
    return 40 * d - ((50, 20)[d < 7], 0)[d < 3]
