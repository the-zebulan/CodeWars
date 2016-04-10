def stairs_in_20(stairs):
    return sum(sum(a) for day in stairs for a in day) * 20
