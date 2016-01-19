def number(bus_stops):
    return sum(on - off for on, off in bus_stops)


assert number([[10, 0], [3, 5], [5, 8]]) == 5
assert number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]) == 17
assert number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]) == 21
