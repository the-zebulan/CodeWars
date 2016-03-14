bus = 8.0
walk = 5.0


def calculator(distance, bus_drive, bus_walk):
    bd = bus_drive / (bus / 60)
    bw = bus_walk / (walk / 60)
    b = bd + bw
    minutes = distance * (walk / 60)
    print 'b: {}\tw: {}'.format(b, minutes)
    if minutes < 0.1 or minutes == b:
        return 'Walk'
    elif minutes > 1.2:
        return 'Bus'
    return 'Bus' if b < minutes else 'Walk'


print calculator(5, 6, 1) == 'Bus'
print calculator(4, 5, 1) == 'Walk'
print calculator(5, 8, 0) == 'Walk'
print calculator(5, 4, 3) == 'Walk'
print calculator(11, 15, 2) == 'Bus'
print calculator(0.6, 0.4, 0) == 'Walk'
