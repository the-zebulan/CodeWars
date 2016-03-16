# bus & walk are pre-defined globals in this kata
bus = 8.0
walk = 5.0


def calculator(distance, bus_drive, bus_walk):
    walk_time = distance / walk * 60
    if walk_time > 120:
        return 'Bus'
    walk_bus_walk = (bus_walk / walk * 60) + (bus_drive / bus * 60)
    return ('Bus', 'Walk')[walk_time < walk_bus_walk or
                           walk_time < 10 or walk_bus_walk == walk_time]
