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
