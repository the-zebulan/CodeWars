def cockroach_speed(km_h):
    return int(km_h / 0.036)  # centimeters per second

assert cockroach_speed(1.08) == 30
assert cockroach_speed(1.09) == 30
assert cockroach_speed(0) == 0
