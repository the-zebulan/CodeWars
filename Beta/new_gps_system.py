def total_kilometers(cons, petrol):
    return round(petrol / float(cons) * 100, 2)


def check_distance(distance, cons, petrol):
    if total_kilometers(cons, petrol) < distance:
        return 'You will need to refuel'
    km_driven = 0
    result = []
    while distance >= 0:
        result.append([km_driven, distance, petrol])
        distance -= 100
        km_driven += 100
        petrol = round(petrol - cons, 2)
    return result

assert total_kilometers(9.3, 87.3) == 938.71
assert total_kilometers(11.7, 63.4) == 541.88
assert total_kilometers(22, 28) == 127.27
assert check_distance(700, 10, 60) == "You will need to refuel"
assert check_distance(467, 12.3, 60) == \
    [[0, 467, 60], [100, 367, 47.7], [200, 267, 35.40],
     [300, 167, 23.10], [400, 67, 10.80]]
